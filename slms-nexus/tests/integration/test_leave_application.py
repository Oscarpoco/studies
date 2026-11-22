"""Integration tests for the leave application process (Task 3.1.2)."""

import sqlite3
from pathlib import Path

import pytest

from src.leave_application.leave_application import leaveApplication

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "database" / "schema" / "schema.sql"


@pytest.fixture()
def temp_db(tmp_path: Path) -> Path:
    db_path = tmp_path / "test_SLMS_Nexus.db"
    conn = sqlite3.connect(db_path)
    conn.executescript(SCHEMA.read_text(encoding="utf-8"))
    conn.execute(
        """
        INSERT INTO Employees
            (FirstName, LastName, Email, Department, JobTitle, DateJoined, AnnualLeaveBalance)
        VALUES ('Test', 'User', 'test.user@nexus.co.za', 'IT', 'Tester', '2024-01-01', 10)
        """
    )
    conn.execute(
        "INSERT INTO LeaveTypes (TypeName, MaxDaysAllowed) VALUES ('Annual Leave', 21)"
    )
    conn.commit()
    conn.close()
    return db_path


def test_valid_leave_saves_pending_and_reduces_balance(temp_db: Path):
    # Mon 2 Mar 2026 – Wed 4 Mar 2026 = 3 working days
    result = leaveApplication(
        employee_id=1,
        leave_type_id=1,
        start_date="2026-03-02",
        end_date="2026-03-04",
        reason="Integration test leave",
        db_path=temp_db,
    )

    assert result["success"] is True
    assert result["number_of_days"] == 3
    assert result["balance"] == 7

    conn = sqlite3.connect(temp_db)
    conn.row_factory = sqlite3.Row
    app_row = conn.execute(
        "SELECT Status, NumberOfDays FROM LeaveApplications WHERE ApplicationID = ?",
        (result["application_id"],),
    ).fetchone()
    emp_row = conn.execute(
        "SELECT AnnualLeaveBalance FROM Employees WHERE EmployeeID = 1"
    ).fetchone()
    conn.close()

    assert app_row["Status"] == "Pending"
    assert app_row["NumberOfDays"] == 3
    assert emp_row["AnnualLeaveBalance"] == 7


def test_insufficient_balance_shows_error(temp_db: Path):
    # Request 5 days while balance is only 10 — first drain to 2 days
    leaveApplication(
        employee_id=1,
        leave_type_id=1,
        start_date="2026-03-02",
        end_date="2026-03-06",
        reason="Use most days",
        db_path=temp_db,
    )
    # Balance now 5. Request another 5-day week → should fail if we use 5 again after reducing
    # After first call balance = 5. Request Mon–Fri again (5 days) with balance 5 should succeed.
    # So set expectation: request more than remaining.
    result = leaveApplication(
        employee_id=1,
        leave_type_id=1,
        start_date="2026-04-06",
        end_date="2026-04-17",  # 10 working days
        reason="Too many days",
        db_path=temp_db,
    )

    assert result["success"] is False
    assert "Insufficient leave balance" in result["message"]
    assert result["balance"] == 5

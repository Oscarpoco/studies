"""Leave application module — balance check, save, update balance."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from src.calculate_working_days.calculate_working_days import calculateWorkingDays
from src.db_connection.db_connection import connect_database


def leaveApplication(
    employee_id: int,
    leave_type_id: int,
    start_date: str,
    end_date: str,
    reason: str,
    db_path: Path | str | None = None,
) -> dict[str, Any]:
    """
    Submit a leave application.

    Returns a result dict with keys: success, message, application_id (optional),
    number_of_days (optional), balance (optional).
    """
    number_of_days = calculateWorkingDays(start_date, end_date)
    if number_of_days == 0:
        return {
            "success": False,
            "message": "Invalid date range. End date must be on or after start date, "
            "and at least one working day is required.",
        }

    conn = connect_database(db_path)
    try:
        employee = conn.execute(
            "SELECT EmployeeID, AnnualLeaveBalance FROM Employees WHERE EmployeeID = ?",
            (employee_id,),
        ).fetchone()

        if employee is None:
            return {"success": False, "message": f"Employee {employee_id} not found."}

        leave_type = conn.execute(
            "SELECT LeaveTypeID FROM LeaveTypes WHERE LeaveTypeID = ?",
            (leave_type_id,),
        ).fetchone()
        if leave_type is None:
            return {"success": False, "message": f"Leave type {leave_type_id} not found."}

        balance = int(employee["AnnualLeaveBalance"])
        if balance < number_of_days:
            return {
                "success": False,
                "message": (
                    f"Insufficient leave balance. Requested {number_of_days} day(s), "
                    f"current balance is {balance}."
                ),
                "balance": balance,
            }

        cursor = conn.execute(
            """
            INSERT INTO LeaveApplications
                (EmployeeID, LeaveTypeID, StartDate, EndDate, NumberOfDays, Reason, Status)
            VALUES (?, ?, ?, ?, ?, ?, 'Pending')
            """,
            (employee_id, leave_type_id, start_date, end_date, number_of_days, reason),
        )
        application_id = cursor.lastrowid

        new_balance = balance - number_of_days
        conn.execute(
            "UPDATE Employees SET AnnualLeaveBalance = ? WHERE EmployeeID = ?",
            (new_balance, employee_id),
        )
        conn.commit()

        return {
            "success": True,
            "message": "Leave application submitted successfully. Status: Pending.",
            "application_id": application_id,
            "number_of_days": number_of_days,
            "balance": new_balance,
        }
    finally:
        conn.close()


# Pseudocode reference (Task 2.1.1):
# FUNCTION leaveApplication(EmployeeID, LeaveTypeID, StartDate, EndDate, Reason)
#     days = calculateWorkingDays(StartDate, EndDate)
#     balance = get employee AnnualLeaveBalance
#     IF balance < days THEN
#         PRINT reject + current balance
#     ELSE
#         SAVE application Status = 'Pending'
#         REDUCE balance by days
#         PRINT success
#     END IF
# END FUNCTION

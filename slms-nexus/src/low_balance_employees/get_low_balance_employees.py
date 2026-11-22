"""Find employees with a low annual leave balance."""

from __future__ import annotations

from pathlib import Path

from src.db_connection.db_connection import connect_database


def getLowBalanceEmployees(db_path: Path | str | None = None) -> list[str]:
    """
    Print and return warning lines for employees with balance <= 5.
    """
    conn = connect_database(db_path)
    messages: list[str] = []
    try:
        # Fixed SQL: space before FROM/WHERE, and <= instead of =<
        query = (
            "SELECT EmployeeID, FirstName, LastName, AnnualLeaveBalance "
            "FROM Employees "
            "WHERE AnnualLeaveBalance <= 5"
        )
        results = conn.execute(query).fetchall()

        if len(results) == 0:
            msg = "No employees with low leave balance."
            print(msg)
            messages.append(msg)
        else:
            for employee in results:
                msg = (
                    f"WARNING: Employee {employee['EmployeeID']} "
                    f"{employee['LastName']} has only "
                    f"{employee['AnnualLeaveBalance']} days left"
                )
                print(msg)
                messages.append(msg)
    finally:
        conn.close()

    return messages


if __name__ == "__main__":
    getLowBalanceEmployees()

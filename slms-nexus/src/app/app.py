"""Flask web UI for the Leave Application screen."""

from pathlib import Path

from flask import Flask, render_template, request

from src.db_connection.db_connection import connect_database
from src.leave_application.leave_application import leaveApplication

TEMPLATE_DIR = Path(__file__).resolve().parents[1] / "templates"

app = Flask(__name__, template_folder=str(TEMPLATE_DIR))


def _load_form_options() -> tuple[list, list]:
    conn = connect_database()
    try:
        employees = conn.execute(
            "SELECT EmployeeID, FirstName, LastName, AnnualLeaveBalance "
            "FROM Employees ORDER BY LastName"
        ).fetchall()
        leave_types = conn.execute(
            "SELECT LeaveTypeID, TypeName FROM LeaveTypes ORDER BY LeaveTypeID"
        ).fetchall()
        return list(employees), list(leave_types)
    finally:
        conn.close()


@app.route("/", methods=["GET", "POST"])
def leave_form():
    message = None
    success = None

    if request.method == "POST":
        result = leaveApplication(
            employee_id=int(request.form["employee_id"]),
            leave_type_id=int(request.form["leave_type_id"]),
            start_date=request.form["start_date"],
            end_date=request.form["end_date"],
            reason=request.form.get("reason", "").strip(),
        )
        message = result["message"]
        success = result["success"]

    employees, leave_types = _load_form_options()
    return render_template(
        "leave_application.html",
        employees=employees,
        leave_types=leave_types,
        message=message,
        success=success,
    )


def main() -> None:
    app.run(host="127.0.0.1", port=5000, debug=True)


if __name__ == "__main__":
    main()

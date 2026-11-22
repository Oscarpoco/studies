# leave_application.py — line by line

Full leave submit flow: count days → read balance → insert → update balance.

| Line | Code | What it does |
|------|------|--------------|
| 3 | `from __future__ import annotations` | Allow modern type hints. |
| 5–6 | `Path`, `Any` | Path typing + flexible return dict. |
| 8 | Import `calculateWorkingDays` | Gets working-day count. |
| 9 | Import `connect_database` | Opens SQLite. |
| 12–19 | `def leaveApplication(...)` | Inputs: emp id, type id, dates, reason, optional DB path. |
| 26 | `number_of_days = calculateWorkingDays(...)` | Count Mon–Fri in range. |
| 27–32 | `if number_of_days == 0` | Bad dates → fail dict, no DB write. |
| 34 | `conn = connect_database(db_path)` | Open DB (real or test file). |
| 35 | `try:` | Ensure close in `finally`. |
| 36–39 | `SELECT ... FROM Employees WHERE EmployeeID = ?` | Load that employee’s ID + balance. `?` = safe parameter. |
| 41–42 | `if employee is None` | No row → fail. |
| 44–47 | `SELECT LeaveTypeID FROM LeaveTypes WHERE ...` | Confirm leave type exists. |
| 48–49 | `if leave_type is None` | Missing type → fail. |
| 51 | `balance = int(...)` | Read current leave days. |
| 52–60 | `if balance < number_of_days` | Not enough days → fail + show balance. |
| 62–69 | `INSERT INTO LeaveApplications ... 'Pending'` | Save new app; status Pending. |
| 70 | `application_id = cursor.lastrowid` | New row’s auto ID. |
| 72 | `new_balance = balance - number_of_days` | Days left after request. |
| 73–76 | `UPDATE Employees SET AnnualLeaveBalance = ?` | Write new balance for that employee. |
| 77 | `conn.commit()` | Save both INSERT + UPDATE permanently. |
| 79–85 | Success return dict | Message + ids + days + new balance. |
| 86–87 | `finally: conn.close()` | Always close connection. |

**Data flow:** Form/API values → day count → `Employees`/`LeaveTypes` reads → if OK, write `LeaveApplications` + update `Employees` → result dict.

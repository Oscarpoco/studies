# get_low_balance_employees.py — line by line

Finds staff with `AnnualLeaveBalance <= 5` and prints warnings.

| Line | Code | What it does |
|------|------|--------------|
| 3 | Future annotations | Type hint support. |
| 5 | `Path` | Optional custom DB path. |
| 7 | `connect_database` | Open SQLite. |
| 10 | `def getLowBalanceEmployees(...)` | Main function. |
| 14 | `conn = connect_database(db_path)` | Connect to DB. |
| 15 | `messages = []` | Collect printed lines to return. |
| 17 | `try:` | Guaranteed close. |
| 18–22 | Build `query` string | SELECT id/name/balance FROM Employees WHERE balance ≤ 5. (Spaces fixed vs Task 2.2 bugs.) |
| 23 | `conn.execute(query).fetchall()` | Run SQL; get all matching rows. |
| 25–28 | `if len(results) == 0` | No low-balance staff → one info message. |
| 30 | `for employee in results` | Loop each returned row. |
| 31–35 | Build warning string | Uses `employee['EmployeeID']`, LastName, balance. |
| 36–37 | `print` + `append` | Show and store message. |
| 38–39 | `finally: conn.close()` | Close DB. |
| 41 | `return messages` | List of strings for tests/callers. |
| 44–45 | `__main__` | Run report when file executed alone. |

**Data flow:** Connect → SELECT low-balance employees → for each row print warning → return list.

# seed.sql — line by line

Loads sample rows so students can query real data.

| Line | Code | What it does |
|------|------|--------------|
| 1 | Comment | File purpose. |
| 3 | `PRAGMA foreign_keys = ON` | Enforce FK rules while inserting. |
| 5 | `INSERT INTO Employees (...columns...)` | List columns we will fill (ID auto). |
| 6 | `VALUES` | Start value rows. |
| 7 | Thabo Molefe row | Finance staff; balance 18. |
| 8 | Aisha Patel row | Finance staff; balance 12. |
| 9 | Johan van Wyk row | IT staff; balance 20. |
| 10 | Lerato Dlamini row | IT staff; balance 5 (low). |
| 12 | `INSERT INTO LeaveTypes (...)` | Add the three leave types. |
| 14 | Annual Leave, 21 | Type 1 (ID becomes 1). |
| 15 | Sick Leave, 30 | Type 2. |
| 16 | Family Responsibility Leave, 3 | Type 3. |
| 18–19 | `INSERT INTO LeaveApplications (...)` | Columns for each application. |
| 21 | App for Emp 1, Type 1 | Approved 5-day annual leave. |
| 22 | App for Emp 2, Type 2 | Pending sick leave. |
| 23 | App for Emp 3, Type 1 | Rejected annual leave. |
| 24 | App for Emp 4, Type 3 | Approved family leave. |
| 25 | App for Emp 1, Type 1 | Pending annual leave. |

**Data flow:** Employees first → LeaveTypes next → LeaveApplications last (needs valid FKs). IDs: Emp 1–4, Types 1–3, Apps 1–5.

# queries.sql — line by line

How each query gets data from `SLMS_Nexus.db`.

## Query 1 — employees by leave balance

| Line | Code | What it does |
|------|------|--------------|
| 3 | `-- 1.1.1 (1)...` | Comment only — labels the question. |
| 4 | `SELECT EmployeeID, FirstName, LastName, Email, AnnualLeaveBalance` | Choose these 5 columns from each matching row. |
| 5 | `FROM Employees` | Read rows from the `Employees` table. |
| 6 | `ORDER BY AnnualLeaveBalance ASC` | Sort so lowest balance is first, highest last. |

**Data flow:** SQLite scans `Employees` → picks the listed fields → sorts by `AnnualLeaveBalance`.

---

## Query 2 — pending applications

| Line | Code | What it does |
|------|------|--------------|
| 8 | `-- 1.1.1 (2)...` | Comment only. |
| 9 | `SELECT ApplicationID, EmployeeID, StartDate, EndDate, NumberOfDays, Reason` | Return these fields for each pending app. |
| 10 | `FROM LeaveApplications` | Read from leave applications. |
| 11 | `WHERE Status = 'Pending'` | Keep only rows where Status is Pending. |

**Data flow:** Scan `LeaveApplications` → filter Status → return the selected columns.

---

## Query 3 — approved days per department

| Line | Code | What it does |
|------|------|--------------|
| 13 | `-- 1.1.1 (3)...` | Comment only. |
| 14 | `SELECT e.Department, SUM(la.NumberOfDays) AS TotalApprovedDays` | Department name + sum of days (named `TotalApprovedDays`). |
| 15 | `FROM LeaveApplications la` | Start from applications; alias `la`. |
| 16 | `INNER JOIN Employees e ON la.EmployeeID = e.EmployeeID` | Link each app to its employee via `EmployeeID`. Only matched pairs stay. |
| 17 | `WHERE la.Status = 'Approved'` | Only approved applications. |
| 18 | `GROUP BY e.Department` | One result row per department; `SUM` adds days in that group. |
| 19 | `ORDER BY TotalApprovedDays DESC` | Highest total days first. |

**Data flow:** Join apps ↔ employees → keep Approved → group by Department → sum days → sort high to low.

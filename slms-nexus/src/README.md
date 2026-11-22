# src/

One folder per module. Open that folder’s README for a line-by-line guide.

| Folder | Gets data from |
|--------|----------------|
| `db_connection/` | Opens `database/SLMS_Nexus.db` |
| `calculate_working_days/` | Dates only (no DB) |
| `leave_application/` | SELECT/INSERT/UPDATE on Employees + LeaveApplications |
| `low_balance_employees/` | SELECT Employees where balance ≤ 5 |
| `app/` | SQL for dropdowns + POST into leaveApplication |
| `templates/` | Receives lists/message from Flask |

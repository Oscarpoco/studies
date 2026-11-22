# leave_application_pseudocode.md

Plain steps matching `leaveApplication()` in code.

| Step | Meaning |
|------|---------|
| 1 Input | Values from form/user. |
| 2 Read balance | SELECT from Employees. |
| 3 Count days | `calculateWorkingDays`. |
| 4 Invalid range | Stop if 0 days. |
| 5 Not enough balance | Reject; show current balance. |
| 6 Enough balance | INSERT Pending + UPDATE balance + success. |

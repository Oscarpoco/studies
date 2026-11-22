# leave_application.html — how it works

Browser form for leave submit. Data comes from Flask (`employees`, `leave_types`, `message`, `success`).

| Part | What it does |
|------|--------------|
| `<form method="post">` | On Submit, sends field values to `/`. |
| Employee `<select name="employee_id">` | Loops `employees` from DB; value = EmployeeID. |
| Leave Type `<select name="leave_type_id">` | Loops `leave_types` from DB; value = LeaveTypeID. |
| `start_date` / `end_date` | User picks dates (`type="date"`). |
| `reason` textarea | Optional text. |
| Submit button | Triggers POST → `leaveApplication` in Python. |
| `{% if message %}` block | Shows success/error text returned from the server. |

**Data flow:** Flask SQL → template variables → HTML dropdowns → user POST → Flask → DB write → message on page.

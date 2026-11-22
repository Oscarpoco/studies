# screen_design.md

Maps the Leave Application UI to data sources.

| UI piece | Data source |
|----------|-------------|
| Employee dropdown | `SELECT` Employees |
| Leave Type dropdown | `SELECT` LeaveTypes |
| Start/End/Reason | User input |
| Submit | POST → `leaveApplication` |
| Message area | Result dict (`success` / `message`) |

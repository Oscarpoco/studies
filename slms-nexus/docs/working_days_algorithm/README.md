# working_days_algorithm.md

Algorithm for `calculateWorkingDays` (Task 2.1.2).

| Step | Meaning |
|------|---------|
| 1 Convert | Turn inputs into dates. |
| 2 Guard | End before start → return 0. |
| 3 Init | count=0, current=start. |
| 4 Loop | Walk each day to endDate. |
| 4a Count | If Mon–Fri, add 1. |
| 5 Return | Total working days. |

No database — dates in, number out.

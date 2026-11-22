# test_calculate_working_days.py — line by line

Four unit tests; no database. Each calls `calculateWorkingDays` and checks the int result.

| Line | Code | What it does |
|------|------|--------------|
| 3 | Import function | Load code under test. |
| 6–8 | `test_five_consecutive_weekdays` | Mon–Fri one week → expect **5**. |
| 11–24 | `test_nine_calendar_days...` | Sat 7 Mar–Sun 15 Mar (9 days, 2 weekends) → expect **5**. |
| 27–29 | `test_same_start_and_end_weekday` | Same Wednesday → expect **1**. |
| 32–33 | `test_end_before_start_returns_zero` | End before start → expect **0**. |

**Data flow:** Hard-coded dates → function → `assert` compares expected vs actual (pytest Pass/Fail).

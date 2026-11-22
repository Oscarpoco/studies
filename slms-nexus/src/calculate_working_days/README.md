# calculate_working_days.py — line by line

Counts Mon–Fri days between two dates (no DB).

## `_to_date`

| Line | Code | What it does |
|------|------|--------------|
| 3–4 | Imports | `date`/`datetime`/`timedelta` + `Union` type. |
| 6 | `DateLike = ...` | Accepts date, datetime, or `"YYYY-MM-DD"` string. |
| 9 | `def _to_date(value)` | Helper: always return a `date`. |
| 10–11 | `if isinstance(..., datetime)` | Strip time → date. |
| 12–13 | `if isinstance(..., date)` | Already a date → return it. |
| 14 | `strptime(..., "%Y-%m-%d")` | Parse string like `2026-03-02`. |

## `calculateWorkingDays`

| Line | Code | What it does |
|------|------|--------------|
| 17 | Function signature | Takes start + end; returns int. |
| 22–23 | `start` / `end` | Convert both inputs to dates. |
| 25–26 | `if end < start: return 0` | Invalid range → 0 (error case). |
| 28–29 | `working_days = 0`, `current = start` | Counter + walk pointer. |
| 30 | `while current <= end` | Inclusive loop through every calendar day. |
| 31–32 | `weekday() < 5` | Mon=0…Fri=4 → count; Sat/Sun skipped. |
| 33 | `current += timedelta(days=1)` | Move to next day. |
| 34 | `return working_days` | Final count. |
| 37–41 | `if __name__ == "__main__"` | Demo prints when file run directly. |

**Data flow:** Dates in → normalize → walk day by day → count weekdays → int out.

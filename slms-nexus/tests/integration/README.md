# test_leave_application.py — line by line

Integration tests use a temporary SQLite DB (not the real student DB).

## Fixture `temp_db`

| Line | Code | What it does |
|------|------|--------------|
| 14–15 | `@pytest.fixture` + `temp_db` | Builds a fresh DB for each test. |
| 16 | `tmp_path / "test_SLMS_Nexus.db"` | Isolated file in pytest temp folder. |
| 17–18 | Connect + `executescript(SCHEMA)` | Create empty tables from schema.sql. |
| 19–25 | INSERT one employee | Balance starts at **10**. |
| 26–28 | INSERT one leave type | Annual Leave. |
| 29–31 | commit + close + return path | Test receives DB path. |

## Test 1 — valid leave

| Line | What it does |
|------|--------------|
| 36–43 | Call `leaveApplication` for 3 working days. |
| 45–47 | Assert success, days=3, balance=7. |
| 49–58 | Re-open DB; SELECT Status/NumberOfDays and employee balance. |
| 60–62 | Assert Status=`Pending`, days=3, balance=7 in DB. |

## Test 2 — insufficient balance

| Line | What it does |
|------|--------------|
| 67–74 | First leave uses 5 days → balance becomes 5. |
| 78–85 | Second request asks for 10 working days. |
| 87–89 | Assert fail message + balance still 5 (no bad write). |

**Data flow:** Temp schema/seed → `leaveApplication` reads/writes → SELECT checks rows → asserts.

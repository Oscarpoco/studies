# tests/

| Folder | What it checks | Data source |
|--------|----------------|-------------|
| `unit/` | `calculateWorkingDays` only | Dates in the test (no DB) |
| `integration/` | Full leave submit | Temp SQLite built in the fixture |

Run: `python -m pytest tests/ -v`  
Each test file README explains every step.

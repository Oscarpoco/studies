# init_db.py — line by line

Creates a fresh `database/SLMS_Nexus.db` from SQL files.

| Line | Code | What it does |
|------|------|--------------|
| 1 | Docstring | Script purpose. |
| 3–4 | Imports | Paths + sqlite3. |
| 6 | `ROOT = ...parents[2]` | Project root (`slms-nexus/`). |
| 7 | `DB_PATH` | Target file `database/SLMS_Nexus.db`. |
| 8 | `SCHEMA` | Path to `schema.sql`. |
| 9 | `SEED` | Path to `seed.sql`. |
| 12 | `def main()` | Setup entry point. |
| 13 | `mkdir(..., exist_ok=True)` | Ensure `database/` exists. |
| 14–15 | Delete old DB if present | Clean rebuild. |
| 17 | `sqlite3.connect(DB_PATH)` | Create new empty DB file + connection. |
| 18 | `try:` | Always close. |
| 19 | `PRAGMA foreign_keys = ON` | Enforce FKs while building. |
| 20 | `executescript(SCHEMA...)` | Run all CREATE TABLE statements. |
| 21 | `executescript(SEED...)` | Run all INSERT sample rows. |
| 22 | `commit()` | Save to disk. |
| 23 | `print(...)` | Confirm path. |
| 24–25 | `finally: close` | Release file lock. |
| 28–29 | `__main__` | Run when: `python scripts/init_db/init_db.py`. |

**Data flow:** Delete old DB → create file → schema creates tables → seed inserts rows → ready for app/queries.

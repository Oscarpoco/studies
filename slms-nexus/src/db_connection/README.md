# db_connection.py — line by line

Opens SQLite and returns a usable connection.

| Line | Code | What it does |
|------|------|--------------|
| 1 | Module docstring | Describes the file. |
| 3–4 | `Path`, `sqlite3` imports | File paths + SQLite driver (built into Python). |
| 6 | `DB_PATH = ... / "SLMS_Nexus.db"` | Default DB file under `database/`. `parents[2]` goes up from this folder to project root. |
| 9 | `def connect_database(...)` | Function students/other modules call. |
| 11 | `path = Path(db_path) if db_path else DB_PATH` | Use a custom path (tests) or the default DB. |
| 12 | `conn = sqlite3.connect(path)` | Open / create the `.db` file and start a session. |
| 13 | `conn.row_factory = sqlite3.Row` | Rows act like dicts: `row["Email"]`. |
| 14 | `PRAGMA foreign_keys = ON` | Enforce FK rules on this connection. |
| 15 | `return conn` | Hand connection to caller (they must `.close()`). |

**Data flow:** Caller → `connect_database()` → SQLite file on disk → connection object for `execute` / `fetch`.

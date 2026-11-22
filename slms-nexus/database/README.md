# database/

SQLite files for SLMS. Each script folder has a line-by-line README.

| Folder / file | Role |
|---------------|------|
| `schema/` | Creates tables + keys |
| `seed/` | Inserts sample rows |
| `queries/` | Three report SELECTs |
| `SLMS_Nexus.db` | Built by `scripts/init_db/init_db.py` |

**How data gets in:** `init_db` runs schema then seed → `.db` file. App/tests/query tools read that file.

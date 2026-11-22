"""Create SLMS_Nexus.db from schema.sql and seed.sql."""

from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "database" / "SLMS_Nexus.db"
SCHEMA = ROOT / "database" / "schema" / "schema.sql"
SEED = ROOT / "database" / "seed" / "seed.sql"


def main() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.executescript(SCHEMA.read_text(encoding="utf-8"))
        conn.executescript(SEED.read_text(encoding="utf-8"))
        conn.commit()
        print(f"Database ready: {DB_PATH}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()

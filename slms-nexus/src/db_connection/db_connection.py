"""Database connection helper for SLMS_Nexus."""

from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).resolve().parents[2] / "database" / "SLMS_Nexus.db"


def connect_database(db_path: Path | str | None = None) -> sqlite3.Connection:
    """Connect to SQLite and enable foreign key checks."""
    path = Path(db_path) if db_path else DB_PATH
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

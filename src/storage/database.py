"""SQLite connection and schema initialization."""
import sqlite3
from pathlib import Path


class Database:
    def __init__(self, db_path: str | Path = "data/students.db") -> None:
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.initialize()

    def connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.db_path, timeout=10)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def initialize(self) -> None:
        with self.connect() as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    student_id TEXT PRIMARY KEY COLLATE NOCASE,
                    full_name TEXT NOT NULL,
                    age INTEGER NOT NULL CHECK(age BETWEEN 15 AND 100),
                    date_of_birth TEXT NOT NULL DEFAULT 'N/A',
                    gender TEXT NOT NULL CHECK(gender IN ('Nam', 'Nữ', 'Khác')),
                    average_score REAL NOT NULL CHECK(average_score BETWEEN 0 AND 10),
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """)

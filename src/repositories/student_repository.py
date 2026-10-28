"""Database operations for student records."""
import sqlite3
from src.models.student import Student
from src.storage.database import Database


class StudentRepository:
    def __init__(self, database: Database) -> None:
        self.database = database

    @staticmethod
    def _to_student(row: sqlite3.Row) -> Student:
        return Student(row["student_id"], row["full_name"], row["age"],
                       row["date_of_birth"], row["gender"], row["average_score"])

    def add(self, student: Student) -> None:
        try:
            with self.database.connect() as connection:
                connection.execute(
                    """INSERT INTO students
                    (student_id, full_name, age, date_of_birth, gender, average_score)
                    VALUES (?, ?, ?, ?, ?, ?)""",
                    (student.student_id, student.full_name, student.age,
                     student.date_of_birth, student.gender, student.average_score))
        except sqlite3.IntegrityError as exc:
            if "UNIQUE constraint failed" in str(exc):
                raise ValueError(f"Mã sinh viên {student.student_id} đã tồn tại.") from exc
            raise ValueError(f"Dữ liệu không hợp lệ: {exc}") from exc

    def get_all(self) -> list[Student]:
        with self.database.connect() as connection:
            rows = connection.execute(
                "SELECT * FROM students ORDER BY student_id COLLATE NOCASE").fetchall()
        return [self._to_student(row) for row in rows]

    def get_by_id(self, student_id: str) -> Student | None:
        with self.database.connect() as connection:
            row = connection.execute(
                "SELECT * FROM students WHERE student_id = ?", (student_id.strip(),)).fetchone()
        return self._to_student(row) if row else None

    def search(self, keyword: str) -> list[Student]:
        pattern = f"%{keyword.strip()}%"
        with self.database.connect() as connection:
            rows = connection.execute(
                """SELECT * FROM students
                   WHERE student_id LIKE ? COLLATE NOCASE
                      OR full_name LIKE ? COLLATE NOCASE
                      OR gender LIKE ? COLLATE NOCASE
                   ORDER BY full_name COLLATE NOCASE""",
                (pattern, pattern, pattern)).fetchall()
        return [self._to_student(row) for row in rows]

    def update(self, original_id: str, student: Student) -> None:
        try:
            with self.database.connect() as connection:
                cursor = connection.execute(
                    """UPDATE students SET student_id=?, full_name=?, age=?,
                       date_of_birth=?, gender=?, average_score=?, updated_at=CURRENT_TIMESTAMP
                       WHERE student_id=?""",
                    (student.student_id, student.full_name, student.age, student.date_of_birth,
                     student.gender, student.average_score, original_id.strip()))
                if cursor.rowcount == 0:
                    raise ValueError(f"Không tìm thấy sinh viên {original_id}.")
        except sqlite3.IntegrityError as exc:
            if "UNIQUE constraint failed" in str(exc):
                raise ValueError(f"Mã sinh viên {student.student_id} đã tồn tại.") from exc
            raise ValueError(f"Dữ liệu không hợp lệ: {exc}") from exc

    def delete(self, student_id: str) -> None:
        with self.database.connect() as connection:
            cursor = connection.execute("DELETE FROM students WHERE student_id = ?", (student_id.strip(),))
            if cursor.rowcount == 0:
                raise ValueError(f"Không tìm thấy sinh viên {student_id}.")

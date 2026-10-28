"""Business logic, sorting, statistics and CSV export."""
import csv
from collections import Counter
from pathlib import Path
from src.models.student import Student
from src.repositories.student_repository import StudentRepository


class StudentManager:
    def __init__(self, repository: StudentRepository) -> None:
        self.repository = repository

    def add_student(self, student: Student) -> None:
        student.validate()
        self.repository.add(student)

    def get_all_students(self) -> list[Student]:
        return self.repository.get_all()

    def get_student(self, student_id: str) -> Student | None:
        return self.repository.get_by_id(student_id)

    def search_students(self, keyword: str) -> list[Student]:
        if not keyword.strip():
            return self.get_all_students()
        return self.repository.search(keyword)

    def update_student(self, original_id: str, student: Student) -> None:
        student.validate()
        self.repository.update(original_id, student)

    def delete_student(self, student_id: str) -> None:
        self.repository.delete(student_id)

    def sort_students(self, criterion: str = "id", descending: bool = False) -> list[Student]:
        keys = {
            "id": lambda s: s.student_id.casefold(),
            "name": lambda s: s.full_name.casefold(),
            "age": lambda s: s.age,
            "score": lambda s: s.average_score,
        }
        if criterion not in keys:
            raise ValueError("Tiêu chí sắp xếp không hợp lệ.")
        return sorted(self.get_all_students(), key=keys[criterion], reverse=descending)

    def get_statistics(self) -> dict:
        students = self.get_all_students()
        if not students:
            return {"total": 0, "average_age": 0, "average_score": 0,
                    "highest": None, "lowest": None, "classifications": {}}
        return {
            "total": len(students),
            "average_age": sum(s.age for s in students) / len(students),
            "average_score": sum(s.average_score for s in students) / len(students),
            "highest": max(students, key=lambda s: s.average_score),
            "lowest": min(students, key=lambda s: s.average_score),
            "classifications": dict(Counter(s.classification for s in students)),
        }

    def export_csv(self, output_path: str | Path = "reports/students_report.csv") -> Path:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(["Mã SV", "Họ tên", "Tuổi", "Ngày sinh", "Giới tính", "Điểm TB", "Xếp loại"])
            for student in self.get_all_students():
                writer.writerow([student.student_id, student.full_name, student.age,
                                 student.date_of_birth, student.gender,
                                 f"{student.average_score:.2f}", student.classification])
        return path

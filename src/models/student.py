"""Student domain model, normalization and validation."""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Student:
    student_id: str
    full_name: str
    age: int
    date_of_birth: str = "N/A"
    gender: str = "Khác"
    average_score: float = 0.0

    def __post_init__(self) -> None:
        self.student_id = self.student_id.strip().upper()
        self.full_name = " ".join(self.full_name.strip().split())
        self.date_of_birth = self.date_of_birth.strip() or "N/A"
        gender_map = {"nam": "Nam", "nữ": "Nữ", "nu": "Nữ", "khác": "Khác", "khac": "Khác"}
        self.gender = gender_map.get(self.gender.strip().casefold(), self.gender.strip())
        try:
            self.age = int(self.age)
            self.average_score = round(float(self.average_score), 2)
        except (TypeError, ValueError) as exc:
            raise ValueError("Tuổi và điểm phải là số hợp lệ.") from exc
        self.validate()

    def validate(self) -> None:
        if not self.student_id:
            raise ValueError("Mã sinh viên không được để trống.")
        if not self.full_name:
            raise ValueError("Họ tên không được để trống.")
        if not 15 <= self.age <= 100:
            raise ValueError("Tuổi phải nằm trong khoảng 15–100.")
        if self.gender not in {"Nam", "Nữ", "Khác"}:
            raise ValueError("Giới tính phải là Nam, Nữ hoặc Khác.")
        if not 0 <= self.average_score <= 10:
            raise ValueError("Điểm trung bình phải nằm trong khoảng 0–10.")
        if self.date_of_birth != "N/A":
            try:
                datetime.strptime(self.date_of_birth, "%d/%m/%Y")
            except ValueError as exc:
                raise ValueError("Ngày sinh phải theo định dạng DD/MM/YYYY.") from exc

    @property
    def classification(self) -> str:
        if self.average_score >= 9:
            return "Xuất sắc"
        if self.average_score >= 8:
            return "Giỏi"
        if self.average_score >= 6.5:
            return "Khá"
        if self.average_score >= 5:
            return "Trung bình"
        if self.average_score >= 3.5:
            return "Yếu"
        return "Kém"

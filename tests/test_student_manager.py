"""Unit tests run against a temporary database."""
import tempfile
import unittest
from pathlib import Path
from src.models.student import Student
from src.storage.database import Database
from src.repositories.student_repository import StudentRepository
from src.services.student_manager import StudentManager


class StudentManagerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        database = Database(Path(self.temp_dir.name) / "students.db")
        self.manager = StudentManager(StudentRepository(database))

    def tearDown(self):
        self.temp_dir.cleanup()

    @staticmethod
    def make_student(student_id="SV001", name="Nguyễn Văn An", score=8.5):
        return Student(student_id, name, 20, "15/03/2006", "Nam", score)

    def test_add_and_read(self):
        self.manager.add_student(self.make_student())
        self.assertEqual(self.manager.get_student("sv001").full_name, "Nguyễn Văn An")

    def test_duplicate_id_rejected(self):
        self.manager.add_student(self.make_student())
        with self.assertRaises(ValueError):
            self.manager.add_student(self.make_student())

    def test_classification(self):
        self.assertEqual(self.make_student(score=9.2).classification, "Xuất sắc")
        self.assertEqual(self.make_student(score=6.5).classification, "Khá")

    def test_search(self):
        self.manager.add_student(self.make_student())
        self.assertEqual(len(self.manager.search_students("nguyễn")), 1)

    def test_update(self):
        self.manager.add_student(self.make_student())
        self.manager.update_student("SV001", self.make_student(score=9.5))
        self.assertEqual(self.manager.get_student("SV001").average_score, 9.5)

    def test_delete(self):
        self.manager.add_student(self.make_student())
        self.manager.delete_student("SV001")
        self.assertIsNone(self.manager.get_student("SV001"))

    def test_invalid_score(self):
        with self.assertRaises(ValueError):
            self.make_student(score=11)

    def test_statistics(self):
        self.manager.add_student(self.make_student(score=8.0))
        self.manager.add_student(self.make_student("SV002", "Trần Thị Bình", 10.0))
        stats = self.manager.get_statistics()
        self.assertEqual(stats["total"], 2)
        self.assertEqual(stats["average_score"], 9.0)

    def test_csv_export(self):
        self.manager.add_student(self.make_student())
        path = Path(self.temp_dir.name) / "report.csv"
        self.manager.export_csv(path)
        self.assertIn("Nguyễn Văn An", path.read_text(encoding="utf-8-sig"))


if __name__ == "__main__":
    unittest.main()

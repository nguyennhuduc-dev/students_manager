"""Vietnamese terminal interface."""
from src.models.student import Student
from src.storage.database import Database
from src.repositories.student_repository import StudentRepository
from src.services.student_manager import StudentManager


class ConsoleApp:
    def __init__(self) -> None:
        self.manager = StudentManager(StudentRepository(Database()))

    @staticmethod
    def _input_int(prompt: str, minimum: int, maximum: int) -> int:
        while True:
            try:
                value = int(input(prompt).strip())
                if minimum <= value <= maximum:
                    return value
            except ValueError:
                pass
            print(f"Vui lòng nhập số nguyên từ {minimum} đến {maximum}.")

    @staticmethod
    def _input_score(prompt: str, current: float | None = None) -> float:
        while True:
            raw = input(prompt).strip().replace(",", ".")
            if not raw and current is not None:
                return current
            try:
                value = float(raw)
                if 0 <= value <= 10:
                    return value
            except ValueError:
                pass
            print("Điểm phải là số từ 0 đến 10.")

    @staticmethod
    def _input_gender(prompt: str = "Giới tính (Nam/Nữ/Khác): ", current: str | None = None) -> str:
        mapping = {"nam": "Nam", "nữ": "Nữ", "nu": "Nữ", "khác": "Khác", "khac": "Khác"}
        while True:
            raw = input(prompt).strip().casefold()
            if not raw and current:
                return current
            if raw in mapping:
                return mapping[raw]
            print("Giới tính không hợp lệ.")

    @staticmethod
    def print_students(students: list[Student]) -> None:
        if not students:
            print("\nKhông có sinh viên phù hợp.")
            return
        headers = ["Mã SV", "Họ tên", "Tuổi", "Ngày sinh", "Giới tính", "Điểm TB", "Xếp loại"]
        rows = [[s.student_id, s.full_name, str(s.age), s.date_of_birth, s.gender,
                 f"{s.average_score:.2f}", s.classification] for s in students]
        widths = [max(len(headers[i]), *(len(row[i]) for row in rows)) for i in range(len(headers))]
        line = "+-" + "-+-".join("-" * width for width in widths) + "-+"
        print("\n" + line)
        print("| " + " | ".join(headers[i].ljust(widths[i]) for i in range(len(headers))) + " |")
        print(line)
        for row in rows:
            print("| " + " | ".join(row[i].ljust(widths[i]) for i in range(len(row))) + " |")
        print(line)
        print(f"Tổng số: {len(students)} sinh viên")

    def add_student(self) -> None:
        try:
            student = Student(
                input("Mã sinh viên: "), input("Họ và tên: "),
                self._input_int("Tuổi (15–100): ", 15, 100),
                input("Ngày sinh (DD/MM/YYYY, bỏ trống nếu chưa có): "),
                self._input_gender(), self._input_score("Điểm trung bình (0–10): "))
            self.manager.add_student(student)
            print("Thêm sinh viên thành công.")
        except ValueError as exc:
            print(f"Không thể thêm: {exc}")

    def update_student(self) -> None:
        original_id = input("Mã sinh viên cần cập nhật: ").strip()
        old = self.manager.get_student(original_id)
        if not old:
            print("Không tìm thấy sinh viên.")
            return
        print("Nhấn Enter để giữ nguyên giá trị hiện tại.")
        new_id = input(f"Mã SV [{old.student_id}]: ").strip() or old.student_id
        name = input(f"Họ tên [{old.full_name}]: ").strip() or old.full_name
        age_raw = input(f"Tuổi [{old.age}]: ").strip()
        try:
            age = int(age_raw) if age_raw else old.age
        except ValueError:
            print("Tuổi không hợp lệ.")
            return
        dob = input(f"Ngày sinh [{old.date_of_birth}]: ").strip() or old.date_of_birth
        gender = self._input_gender(f"Giới tính [{old.gender}]: ", old.gender)
        score = self._input_score(f"Điểm TB [{old.average_score}]: ", old.average_score)
        try:
            self.manager.update_student(original_id, Student(new_id, name, age, dob, gender, score))
            print("Cập nhật sinh viên thành công.")
        except ValueError as exc:
            print(f"Không thể cập nhật: {exc}")

    def delete_student(self) -> None:
        student_id = input("Mã sinh viên cần xóa: ").strip()
        student = self.manager.get_student(student_id)
        if not student:
            print("Không tìm thấy sinh viên.")
            return
        self.print_students([student])
        if input("Xác nhận xóa? (c/k): ").strip().casefold() == "c":
            try:
                self.manager.delete_student(student_id)
                print("Đã xóa sinh viên.")
            except ValueError as exc:
                print(exc)
        else:
            print("Đã hủy thao tác.")

    def show_statistics(self) -> None:
        stats = self.manager.get_statistics()
        if not stats["total"]:
            print("Chưa có dữ liệu để thống kê.")
            return
        print("\n--- THỐNG KÊ SINH VIÊN ---")
        print(f"Tổng sinh viên : {stats['total']}")
        print(f"Tuổi trung bình: {stats['average_age']:.1f}")
        print(f"Điểm trung bình: {stats['average_score']:.2f}")
        print(f"Điểm cao nhất  : {stats['highest'].full_name} ({stats['highest'].average_score:.2f})")
        print(f"Điểm thấp nhất : {stats['lowest'].full_name} ({stats['lowest'].average_score:.2f})")
        print("Phân bố học lực:")
        for name, count in sorted(stats["classifications"].items()):
            print(f"  {name}: {count}")

    def sort_menu(self) -> None:
        print("1. Mã SV A–Z\n2. Họ tên A–Z\n3. Điểm cao xuống thấp\n4. Điểm thấp lên cao\n5. Tuổi tăng dần")
        choice = input("Chọn kiểu sắp xếp: ").strip()
        choices = {"1": ("id", False), "2": ("name", False), "3": ("score", True),
                   "4": ("score", False), "5": ("age", False)}
        if choice not in choices:
            print("Lựa chọn không hợp lệ.")
            return
        criterion, descending = choices[choice]
        self.print_students(self.manager.sort_students(criterion, descending))

    def export_report(self) -> None:
        try:
            path = self.manager.export_csv()
            print(f"Đã xuất báo cáo: {path.resolve()}")
        except OSError as exc:
            print(f"Không thể xuất báo cáo: {exc}")

    def run(self) -> None:
        actions = {
            "1": self.add_student,
            "2": lambda: self.print_students(self.manager.get_all_students()),
            "3": lambda: self.print_students(self.manager.search_students(input("Từ khóa tìm kiếm: "))),
            "4": self.update_student, "5": self.delete_student,
            "6": self.sort_menu, "7": self.show_statistics, "8": self.export_report,
        }
        while True:
            print("\n" + "=" * 56)
            print("       STUDENT MANAGEMENT SYSTEM")
            print("        HỆ THỐNG QUẢN LÝ SINH VIÊN")
            print("=" * 56)
            print("1. Thêm sinh viên\n2. Xem danh sách\n3. Tìm kiếm sinh viên\n4. Cập nhật sinh viên")
            print("5. Xóa sinh viên\n6. Sắp xếp danh sách\n7. Thống kê học lực\n8. Xuất báo cáo CSV\n0. Thoát")
            choice = input("Chọn chức năng: ").strip()
            if choice == "0":
                print("Dữ liệu SQLite đã được lưu. Tạm biệt!")
                break
            try:
                action = actions.get(choice)
                if action:
                    action()
                else:
                    print("Lựa chọn không hợp lệ.")
            except ValueError as exc:
                print(f"Thao tác không thành công: {exc}")
            input("\nNhấn Enter để tiếp tục...")

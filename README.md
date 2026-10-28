# Student Management System

Hệ thống quản lý sinh viên bằng Python theo hướng OOP, giao diện Terminal tiếng Việt và SQLite để lưu dữ liệu lâu dài.

## Tính năng
- Thêm, xem, tìm kiếm, cập nhật và xóa sinh viên.
- Chặn mã sinh viên trùng; chuẩn hóa mã thành chữ in hoa.
- Kiểm tra tuổi (15–100), điểm (0–10), giới tính và ngày sinh `DD/MM/YYYY`.
- Tự động xếp loại học lực.
- Sắp xếp theo mã, họ tên, tuổi hoặc điểm.
- Thống kê số lượng, tuổi/điểm trung bình, điểm cao nhất/thấp nhất và phân bố học lực.
- Lưu dữ liệu trong SQLite sau khi thoát ứng dụng.
- Xuất CSV tương thích Excel.
- Kiểm thử tự động bằng `unittest` với database tạm.

## Yêu cầu
- Python 3.10 trở lên (khuyến nghị Python 3.11+).
- Không cần cài thư viện bên ngoài.

## Cấu trúc
```text
students_manager/
├── main.py
├── src/models/student.py
├── src/storage/database.py
├── src/repositories/student_repository.py
├── src/services/student_manager.py
├── src/ui/console.py
└── tests/test_student_manager.py
```

## Chạy trên Windows / VS Code
Mở Terminal tại thư mục gốc dự án:
```powershell
python --version
python main.py
```
Database tự tạo tại `data/students.db`.

## Chạy kiểm thử
```powershell
python -m unittest discover -s tests -v
```

## Xuất báo cáo
Trong menu, chọn `8. Xuất báo cáo CSV`. File mặc định: `reports/students_report.csv`, dùng UTF-8 BOM để Excel hiển thị tiếng Việt tốt.

## Kiến trúc OOP
- **Model:** `Student` chuẩn hóa dữ liệu, xác thực và xếp loại.
- **Repository:** truy vấn SQL có tham số, quản lý thao tác dữ liệu.
- **Service:** nghiệp vụ, tìm kiếm, sắp xếp, thống kê và xuất CSV.
- **Database:** schema và kết nối SQLite.
- **UI:** nhập/xuất Terminal, không chứa truy vấn SQL.

> Đây là project học tập chạy cục bộ, chưa có đăng nhập/phân quyền hoặc đồng bộ nhiều máy. Hãy chạy `python main.py` từ thư mục gốc.
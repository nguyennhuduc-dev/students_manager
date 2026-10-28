# 🎓 Hệ thống Quản lý Sinh viên — Python



## 📌 Giới thiệu

**Hệ thống Quản lý Sinh viên** là mini-project được xây dựng để thực hành các kiến thức Python cơ bản.

Dữ liệu sinh viên được lưu dưới dạng:

```python
[mã_sv, họ_tên, tuổi, ngày_sinh, giới_tính, điểm_tb]
```

Project hỗ trợ các chức năng quản lý sinh viên như thêm, xem, tìm kiếm, cập nhật, xóa, sắp xếp, thống kê và xuất báo cáo.

---

## ✨ Chức năng

| STT | Chức năng | Mô tả |
|---|---|---|
| 1 | 📝 Thêm sinh viên | Thêm một hoặc nhiều sinh viên |
| 2 | 📋 Xem danh sách | Hiển thị toàn bộ danh sách |
| 3 | 🔍 Tìm kiếm | Tìm theo mã, tên, giới tính, xếp loại |
| 4 | ✏️ Cập nhật | Cập nhật thông tin sinh viên |
| 5 | 🗑️ Xóa | Xóa sinh viên theo mã |
| 6 | 📊 Sắp xếp | Sắp xếp theo nhiều tiêu chí |
| 7 | 📈 Thống kê | Thống kê và phân loại sinh viên |
| 8 | 📄 Xuất báo cáo | Hiển thị báo cáo tổng hợp |

---

## 🧑‍🎓 Thông tin sinh viên

Mỗi sinh viên gồm:

- **Mã sinh viên**
- **Họ và tên**
- **Tuổi**
- **Ngày sinh**
- **Giới tính**
- **Điểm trung bình**

Ví dụ:

```python
["SV001", "Nguyễn Văn An", 20, "15/03/2006", "Nam", 8.5]
```

---

## 🏆 Xếp loại học lực

| Điểm | Xếp loại |
|---:|---|
| ≥ 9.0 | Xuất sắc |
| ≥ 8.0 | Giỏi |
| ≥ 6.5 | Khá |
| ≥ 5.0 | Trung bình |
| ≥ 3.5 | Yếu |
| < 3.5 | Kém |

---

## 🔎 Tìm kiếm

Hệ thống hỗ trợ tìm kiếm theo:

```text
1. Mã sinh viên
2. Họ tên
3. Giới tính
4. Xếp loại học lực
```

Tìm kiếm theo họ tên có thể sử dụng từ khóa.

Ví dụ:

```text
Nhập tên cần tìm: nguyễn
```

---

## 📊 Sắp xếp

Có thể sắp xếp danh sách theo:

- Họ tên A → Z
- Họ tên Z → A
- Điểm trung bình cao → thấp
- Điểm trung bình thấp → cao
- Tuổi tăng dần
- Tuổi giảm dần
- Mã sinh viên tăng dần

---

## 📈 Thống kê

Chương trình cung cấp các thông tin:

- Tổng số sinh viên
- Số lượng Nam / Nữ / Khác
- Tuổi trung bình
- Tuổi nhỏ nhất
- Tuổi lớn nhất
- Điểm trung bình chung
- Điểm cao nhất
- Điểm thấp nhất
- Tỷ lệ đạt từ 5.0 trở lên
- Số lượng sinh viên theo từng xếp loại
- Sinh viên có điểm cao nhất
- Sinh viên có điểm thấp nhất

---

## 📄 Xuất báo cáo

Chức năng báo cáo hiển thị:

1. Danh sách sinh viên
2. Thông tin xếp loại
3. Danh sách sinh viên theo từng nhóm học lực

Các nhóm gồm:

```text
Xuất sắc
Giỏi
Khá
Trung bình
Yếu
Kém
```

---

## 🧪 Dữ liệu mẫu

Project có sẵn dữ liệu mẫu để kiểm tra nhanh chương trình.

Khi khởi động, chương trình sẽ hỏi:

```text
Nạp dữ liệu mẫu để thử nghiệm? (c/k):
```

Nếu chọn `c`, hệ thống sẽ tự động nạp dữ liệu mẫu.

---

## 🛠️ Công nghệ sử dụng

- 🐍 Python 3
- 💻 Console / Terminal
- `list`
- `for`
- `while`
- `if / elif / else`
- `function`
- `lambda`
- `sort()`
- Module `os`

Project **không yêu cầu cài đặt thư viện bên ngoài**.

---

## 📂 Cấu trúc project

```text
Student-Management/
│
├── main.py
└── README.md
```

### `main.py`

Chứa toàn bộ mã nguồn của hệ thống quản lý sinh viên.

### `README.md`

Tài liệu giới thiệu, hướng dẫn sử dụng và thông tin về project.

---

## 🚀 Cài đặt

### 1. Kiểm tra Python

```bash
python --version
```

Hoặc trên Windows:

```bash
py --version
```

### 2. Clone repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

### 3. Di chuyển vào thư mục project

```bash
cd Student-Management
```

### 4. Chạy chương trình

```bash
python main.py
```

Trên Windows:

```bash
py main.py
```

---

## 🎯 Kiến thức đã thực hành

Project giúp thực hành:

```text
Python cơ bản
      ↓
Biến & kiểu dữ liệu
      ↓
List
      ↓
List of Lists
      ↓
Điều kiện
      ↓
Vòng lặp
      ↓
Function
      ↓
Validation
      ↓
Tìm kiếm
      ↓
Sắp xếp
      ↓
Thống kê
      ↓
CRUD
      ↓
Project thực tế
```

---

## 🔮 Hướng phát triển

Trong tương lai có thể phát triển thêm:

- [ ] Lưu dữ liệu bằng JSON
- [ ] Lưu dữ liệu bằng CSV
- [ ] Kết nối SQLite
- [ ] Kết nối SQL Server
- [ ] Xây dựng giao diện GUI
- [ ] Xây dựng Web Application
- [ ] Đăng nhập và phân quyền
- [ ] Quản lý lớp học
- [ ] Quản lý môn học
- [ ] Quản lý điểm
- [ ] Xuất Excel
- [ ] Xuất PDF

---

## 👨‍💻 Tác giả

**Nguyễn Như Đức**

🎓 Sinh viên ngành **Công nghệ thông tin**

📚 Python — Week 05 Mini Project

---

## 📜 License

Project được thực hiện với mục đích **học tập và thực hành Python**.

Bạn có thể sử dụng và chỉnh sửa project cho mục đích học tập cá nhân.

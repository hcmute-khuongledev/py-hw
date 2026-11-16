# Python Homework

Quản lý bài tập Python theo từng buổi trong cùng một project. Tên thư mục, file và biến dùng tiếng Anh; tài liệu hướng dẫn bằng tiếng Việt.

## Cách 1: Vào container để chạy nhiều bài bằng `python` (Recommended)

Bật Docker Desktop. Tại terminal trên máy, mở đúng thư mục project chứa `docker-compose.yaml` (ví dụ `D:\HCMUTE\Python\py-hw`), tạo container chạy nền rồi vào Bash:

```sh
docker compose build
docker compose run -d --name py-hw python sleep infinity
docker exec -it py-hw bash
```

Khi đã vào container, thư mục hiện tại là `/app`. Mở menu của session, nhập số bài để chạy và nhập `0` để thoát:

```sh
python exercise/homework/session_01/main.py
python exercise/homework/session_02/main.py
python exercise/homework/session_03/main.py
```

Gõ `exit` để quay về terminal trên máy. Container vẫn chạy, lần sau vào lại bằng `docker exec -it py-hw bash`. Khi học xong, dọn container tại terminal trên máy:

```sh
docker stop py-hw
docker rm py-hw
```

Nếu báo tên `py-hw` đã tồn tại, dùng lệnh `exec` để vào container đang chạy; nếu container đã dừng, chạy `docker start py-hw` trước. Sửa code trên máy rồi chạy lại ngay trong container, không cần build lại.


## Khi chuyển thư mục project hoặc container không tìm thấy source

Container giữ đường dẫn mount tại thời điểm tạo. Nếu di chuyển hoặc đổi tên thư mục trên Windows, `docker start` không cập nhật đường dẫn đó. Ví dụ container cũ mount `D:\HCMUTE\Lập trình Python\py_hw` sẽ không tự chuyển sang `D:\HCMUTE\Python\py-hw`.

Nếu gặp `can't open file ... No such file or directory`, thoát Bash bằng `exit`, rồi tại PowerShell mở thư mục project hiện tại và kiểm tra mount:

```powershell
docker inspect py-hw --format '{{json .Mounts}}'
```

`Source` phải là thư mục project hiện tại và `Destination` là `/app`. Nếu đường dẫn sai, tạo lại container từ đúng thư mục:

```powershell
cd D:\HCMUTE\Python\py-hw
docker stop py-hw
docker rm py-hw
docker compose run -d --name py-hw python sleep infinity
docker exec -it py-hw bash
```

Lệnh xóa container không xóa source trên Windows, nhưng dữ liệu chỉ lưu bên trong container sẽ mất; lưu kết quả cần giữ trong `/app/outputs` trước khi xóa. Nếu clone project ở nơi khác, thay đường dẫn `cd` tương ứng.

Trong Bash, kiểm tra rồi chạy lại:

```sh
ls /app/exercise/homework
python /app/exercise/homework/session_03/main.py
```

Chỉ chuyển thư mục source thì không cần build lại image. Nếu chưa build image hoặc đã thay đổi thư viện/Dockerfile, chạy `docker compose build` trước khi tạo lại container.

## Cách 2: Chạy nhanh bằng Docker

Máy chỉ cần Git và Docker có Docker Compose, không cần cài Python hay kích hoạt `.venv`. Sau khi clone, mở terminal tại thư mục chứa `docker-compose.yaml` và bật Docker:

```sh
docker compose build
docker compose run --rm python
docker compose run --rm python python exercise/homework/session_01/main.py
docker compose run --rm python python exercise/homework/session_02/main.py
docker compose run --rm python python exercise/homework/session_03/main.py
```

Lệnh chạy mặc định dùng `main.py` để kiểm tra môi trường. Xem [hướng dẫn build và chạy Docker](docs/DOCKER.md).

## Cấu trúc project

```text
py-hw/
|-- exercise/
|   |-- classwork/
|   `-- homework/
|       |-- session_01/
|       |   |-- main.py        # Menu: 13 exercises
|       |   |-- README.md
|       |   `-- exercise_*.py
|       `-- session_02/
|           |-- main.py        # Menu: 15 exercises
|           |-- README.md
|           `-- exercise_*.py
|-- datasets/
|-- outputs/
|-- docs/
|-- main.py
|-- requirements.txt
|-- Dockerfile
|-- docker-compose.yaml
`-- .dockerignore
```

## Quy ước thêm bài tập

1. Tạo `exercise/homework/session_02/`, `exercise/homework/session_03/`… Dùng hai chữ số để dễ sắp xếp.
2. Mỗi buổi có `README.md` và một `main.py` chứa các hàm `exercise_01()`, `exercise_02()`… cùng menu. Khi thêm bài, viết hàm trong `main.py` và thêm cặp tên bài, hàm vào `EXERCISES`. Các file bài tập cũ được giữ để tự xóa; menu không phụ thuộc vào chúng.
3. Có thể thêm mô tả tiếng Anh vào tên file: `exercise_03_sales_analysis.py`.
4. Bài cần nhiều file đặt trong thư mục riêng, ví dụ `session_02/exercise_03/main.py`.
5. Dữ liệu chung đặt trong `datasets/`; dữ liệu riêng đặt trong `session_02/data/`. Kết quả sinh ra lưu trong `outputs/`.

Chạy bài mới từ thư mục gốc:

```sh
docker compose run --rm python python exercise/homework/session_02/main.py
```

Với bài nằm ngay trong `session_XX/`, xác định đường dẫn dữ liệu như sau:

```python
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATASETS_DIR = PROJECT_ROOT / "datasets"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
OUTPUTS_DIR.mkdir(exist_ok=True)
```

Nếu file bài tập nằm sâu hơn một cấp, điều chỉnh `parents` tương ứng. Tránh ghi đường dẫn tuyệt đối của máy cá nhân vào code.


## Bài tập theo buổi

- [Session 01 — Các khái niệm cơ bản](exercise/homework/session_01/README.md)
- [Session 02 — Kiểu dữ liệu và rẽ nhánh](exercise/homework/session_02/README.md)
- [Session 03 — Vòng lặp và danh sách (24 câu)](exercise/homework/session_03/README.md)

Chạy menu bài 3 trong container: `python exercise/homework/session_03/main.py`.
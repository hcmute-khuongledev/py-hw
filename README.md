# Python Homework

Quản lý bài tập Python theo từng buổi trong cùng một project. Tên thư mục, file và biến dùng tiếng Anh; tài liệu hướng dẫn bằng tiếng Việt.

## Cách 1: Vào container để chạy nhiều bài bằng `python` (Recommended)

Tại terminal trên máy, tạo container chạy nền rồi vào shell bằng `exec`:

```sh
docker compose build
docker compose run -d --name py-hw python sleep infinity
docker exec -it py-hw sh
```

Khi đã vào container, thư mục hiện tại là `/app`. Chạy từng bài và nhập dữ liệu theo yêu cầu:

```sh
python exercises/session_01/exercise_01.py
python exercises/session_02/exercise_15.py
...
```

Gõ `exit` để quay về terminal trên máy. Container vẫn chạy, lần sau vào lại bằng `docker exec -it py-hw sh`. Khi học xong, dọn container tại terminal trên máy:

```sh
docker stop py-hw
docker rm py-hw
```

Nếu báo tên `py-hw` đã tồn tại, dùng lệnh `exec` để vào container đang chạy; nếu container đã dừng, chạy `docker start py-hw` trước. Sửa code trên máy rồi chạy lại ngay trong container, không cần build lại.


## Cách 2: Chạy nhanh bằng Docker

Máy chỉ cần Git và Docker có Docker Compose, không cần cài Python hay kích hoạt `.venv`. Sau khi clone, mở terminal tại thư mục chứa `docker-compose.yaml` và bật Docker:

```sh
docker compose build
docker compose run --rm python
docker compose run --rm python python exercises/session_01/exercise_01.py
docker compose run --rm python python exercises/session_01/exercise_02.py
...
```

Lệnh chạy mặc định dùng `main.py` để kiểm tra môi trường. Xem [hướng dẫn build và chạy Docker](docs/DOCKER.md).

## Cấu trúc project

```text
py-hw/
├── exercises/
│   └── session_01/
│       ├── README.md          # Đề bài và ghi chú buổi học
│       ├── exercise_01.py
│       └── exercise_02.py
├── datasets/                 # Dữ liệu dùng chung
├── outputs/                  # Kết quả và biểu đồ (không commit)
├── docs/
│   └── DOCKER.md
├── main.py                   # Kiểm tra môi trường
├── requirements.txt          # Thư viện dùng chung
├── Dockerfile
├── docker-compose.yaml
└── .dockerignore
```

## Quy ước thêm bài tập

1. Tạo `exercises/session_02/`, `exercises/session_03/`… Dùng hai chữ số để dễ sắp xếp.
2. Mỗi buổi có `README.md` ghi đề bài và các file `exercise_01.py`, `exercise_02.py`… Mỗi bài chạy độc lập, đặt logic trong `main()` và gọi qua `if __name__ == "__main__":`.
3. Có thể thêm mô tả tiếng Anh vào tên file: `exercise_03_sales_analysis.py`.
4. Bài cần nhiều file đặt trong thư mục riêng, ví dụ `session_02/exercise_03/main.py`.
5. Dữ liệu chung đặt trong `datasets/`; dữ liệu riêng đặt trong `session_02/data/`. Kết quả sinh ra lưu trong `outputs/`.

Chạy bài mới từ thư mục gốc:

```sh
docker compose run --rm python python exercises/session_02/exercise_01.py
```

Với bài nằm ngay trong `session_XX/`, xác định đường dẫn dữ liệu như sau:

```python
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATASETS_DIR = PROJECT_ROOT / "datasets"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
OUTPUTS_DIR.mkdir(exist_ok=True)
```

Nếu file bài tập nằm sâu hơn một cấp, điều chỉnh `parents` tương ứng. Tránh ghi đường dẫn tuyệt đối của máy cá nhân vào code.

# Hướng dẫn build và chạy Python bằng Docker

## 1. Chuẩn bị

- Cài Git để clone source.
- Windows/macOS: cài và mở Docker Desktop. Trên Windows dùng Linux containers và hoàn tất thiết lập WSL 2 nếu Docker yêu cầu.
- Linux: cài Docker Engine và Docker Compose plugin.
- Không cần cài Python, pip hoặc tạo `.venv` trên máy. Image cung cấp Python 3.12 và các thư viện trong `requirements.txt`.
- Lần build đầu cần Internet để tải image và thư viện.

Kiểm tra:

```sh
docker version
docker compose version
```

`docker version` cần hiển thị được cả Client và Server.

## 2. Clone và build

Clone repository bằng URL của bạn rồi mở terminal trong thư mục source vừa clone, nơi có `Dockerfile` và `docker-compose.yaml`.

```sh
docker compose build
```

Docker tải image Python và cài các thư viện. Bước cài thư viện được cache nếu `requirements.txt` chưa thay đổi.

## 3. Chạy từng bài

Chạy `main.py` để kiểm tra môi trường:

```sh
docker compose run --rm python
```

Chạy bài cụ thể:

```sh
docker compose run --rm python python exercises/session_01/exercise_01.py
docker compose run --rm python python exercises/session_01/exercise_02.py
```

`python` đầu tiên là tên service trong Compose; `python` thứ hai là chương trình trong container. `--rm` xóa container sau khi chạy xong. Source và kết quả lưu trong project vẫn còn.

Bài dùng `input()` cho phép nhập trực tiếp trong terminal. Khi truyền dữ liệu qua pipe hoặc chạy trong CI, thêm `-T`. Ví dụ PowerShell:

```powershell
"An" | docker compose run --rm -T python python exercises/session_01/exercise_01.py
```

Mở Python tương tác hoặc shell trong container:

```sh
docker compose run --rm python python
docker compose run --rm python sh
```

Thoát Python bằng `exit()`, thoát shell bằng `exit`.

### Vào container bằng `exec` để chạy nhiều bài liên tiếp

Tại terminal trên máy, tạo một container chạy nền và mở shell:

```sh
docker compose run -d --name py-hw python sleep infinity
docker exec -it py-hw sh
```

`sleep infinity` giữ container chạy để có thể dùng `exec`; chạy `main.py` mặc định sẽ kết thúc ngay nên không dùng để giữ container. Container này dùng image và volume của service `python`.

Trong shell container, chạy bằng lệnh Python thông thường:

```sh
python exercises/session_01/exercise_01.py
python exercises/session_02/exercise_15.py
cd /app/exercises/session_02
python exercise_08.py
python exercise_10.py
```

Nhập dữ liệu rồi nhấn Enter theo yêu cầu từng bài. Để mở Python tương tác, gõ `python`; gõ `exit()` để quay lại shell.

Gõ `exit` để thoát shell về máy. Container vẫn chạy; lần sau chỉ cần:

```sh
docker exec -it py-hw sh
```

Nếu container đã dừng, chạy `docker start py-hw` trước. Nếu tên đã tồn tại, dùng lại container thay vì chạy lệnh tạo mới.

Khi học xong, chạy trên máy để dừng và xóa container:

```sh
docker stop py-hw
docker rm py-hw
```

Source và kết quả trong thư mục project vẫn được giữ lại. Khi thay đổi thư viện hoặc Dockerfile, build lại image rồi dừng, xóa và tạo lại container này để dùng image mới.

## 4. Quy trình làm bài

1. Bật Docker.
2. Thêm hoặc sửa bài trong `exercises/session_XX/`.
3. Chạy bài bằng lệnh ở trên, thay đường dẫn bằng file cần chạy.
4. Xem kết quả trong terminal hoặc `outputs/`.

Compose gắn thư mục project vào `/app` trong container. Sửa code hoặc dataset rồi chạy lại ngay, không cần build lại. Dùng dấu `/` cho đường dẫn trong container, kể cả khi dùng Windows.

## 5. Thêm thư viện

Thêm thư viện vào `requirements.txt`, sau đó:

```sh
docker compose build
```

Chạy lại bài như bình thường. Cài pip trực tiếp trong container tạm sẽ mất khi container bị xóa. Requirements hiện chưa cố định phiên bản nên các lần build mới có thể lấy phiên bản thư viện khác; dùng `package==version` khi cần cố định môi trường cho môn học.

## 6. Lưu biểu đồ

Image đặt `MPLBACKEND=Agg` để xuất ảnh mà không cần giao diện đồ họa. Dùng `savefig()` để lưu kết quả thay cho mở cửa sổ bằng `show()`:

```python
from pathlib import Path
import matplotlib.pyplot as plt

output_dir = Path("outputs")  # Thư mục làm việc mặc định: /app
output_dir.mkdir(exist_ok=True)
plt.plot([1, 2, 3], [2, 4, 6])
plt.savefig(output_dir / "session_01_exercise_01.png", bbox_inches="tight")
plt.close()
```

Mở ảnh trong `outputs/` trên máy bằng VS Code hoặc trình xem ảnh. Các file kết quả được bỏ qua bởi Git; nếu bài yêu cầu nộp kết quả, điều chỉnh `.gitignore` tương ứng.

## 7. Dùng Docker thuần

Nếu không dùng Compose:

```sh
docker build -t py-hw .
docker run --rm py-hw
docker run --rm -it py-hw python exercises/session_01/exercise_01.py
```

Cách này chạy source đã copy vào image khi build. Cần build lại khi sửa source; kết quả chỉ lưu trong container sẽ mất khi container bị xóa. Dùng Compose để đồng bộ source và kết quả với máy.

## 8. Xử lý lỗi

- **Cannot connect / Access is denied / docker_engine**: mở Docker Desktop, chờ Engine sẵn sàng rồi kiểm tra `docker version`. Nếu vẫn lỗi quyền, kiểm tra quyền truy cập Docker Desktop của tài khoản Windows.
- **Không tìm thấy file**: chạy từ thư mục gốc và kiểm tra đường dẫn bài tập.
- **ModuleNotFoundError**: thêm thư viện vào `requirements.txt` rồi build lại.
- **Không tải được image/thư viện**: kiểm tra mạng, proxy/VPN rồi thử build lại.
- **Lỗi gắn thư mục trên Windows**: kiểm tra quyền chia sẻ thư mục/ổ đĩa trong Docker Desktop. Compose dùng `.:/app` để tránh phải nhập đường dẫn tuyệt đối chứa khoảng trắng hoặc tiếng Việt.
- **File kết quả thuộc root trên Linux**: từ shell Linux, có thể dùng `docker compose run --rm --user "$(id -u):$(id -g)" python python exercises/session_01/exercise_02.py`. Cú pháp này không dùng trong PowerShell.

### Lỗi `failed to fetch anonymous token` / `wsarecv`

Nếu kết nối tới `auth.docker.io` bị ngắt khi tải `python:3.12-slim`, thử tải image riêng rồi build lại:

```sh
docker pull python:3.12-slim
docker compose build
```

Nếu vẫn lỗi, thử mạng khác (ví dụ hotspot điện thoại) để kiểm tra đường truyền, hoặc kiểm tra VPN/proxy đang dùng. Với mạng bắt buộc proxy, cấu hình proxy trong Docker Desktop → Settings → Resources → Proxies, sau đó Apply & Restart. Firewall/proxy cần cho phép HTTPS tới `auth.docker.io` và `registry-1.docker.io`; xem [danh sách tên miền Docker cần truy cập](https://docs.docker.com/desktop/enterprise/allow-list/).

Thông báo này là lỗi kết nối khi lấy token, không phải bằng chứng mật khẩu sai hoặc image không tồn tại. Không cần đổi phiên bản Python hay xóa dữ liệu Docker để xử lý.

## Tham khảo

- [Python Official Image](https://hub.docker.com/_/python)
- [Docker Compose run](https://docs.docker.com/reference/cli/docker/compose/run/)

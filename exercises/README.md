# Danh sách buổi học

- [Session 01 — Các khái niệm cơ bản (13 bài)](session_01/README.md)
- [Session 02 — Kiểu dữ liệu và cấu trúc rẽ nhánh (15 bài)](session_02/README.md)

Các bài mẫu ban đầu đã được thay bằng lời giải theo đề trong `docs/`. Xem cách giải và lệnh chạy tại README của từng buổi.

## Ví dụ chạy

Chạy lệnh từ thư mục gốc project.

| File | Nội dung |
| --- | --- |
| `session_01/exercise_01.py` | Tính tiền trước thuế, thuế và sau thuế |
| `session_01/exercise_02.py` | Tính trung bình ba số nguyên |

Chạy từ thư mục gốc project:

```sh
docker compose run --rm python python exercises/session_01/exercise_01.py
docker compose run --rm python python exercises/session_01/exercise_02.py
```

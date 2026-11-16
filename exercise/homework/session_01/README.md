# Session 01 — Các khái niệm cơ bản

Toàn bộ lời giải và menu nằm trong `main.py`, mỗi bài là một hàm `exercise_XX()`. Các file `exercise_XX.py` cũ được giữ lại để bạn tự xóa; menu không còn sử dụng chúng.

Đề bài: [bài 1](../../../docs/bai_1_cac-khai-niem-co-ban_HW.md).

| Bài | Function in `main.py` | Cách giải |
| --- | --- | --- |
| 01 | `exercise_01()` | Trước thuế = đơn giá × số lượng; thuế = trước thuế × `TAX_RATE`; sau thuế = trước thuế + thuế. |
| 02 | `exercise_02()` | Trung bình cộng = tổng ba số nguyên chia 3. Nhập ba số trên cùng một dòng. |
| 03 | `exercise_03()` | Tách hàng trăm bằng `// 100`, hàng chục bằng `// 10 % 10`, đơn vị bằng `% 10`; lấy trung bình, in 2 chữ số thập phân. |
| 04 | `exercise_04()` | Cộng năm chữ số, lấy phần dư chia 10 để tính số nút. |
| 05 | `exercise_05()` | Hoán đổi bằng phép gán `first, second = second, first`. |
| 06 | `exercise_06()` | In số liền trước `k - 1`, rồi số liền sau `k + 1`. |
| 07 | `exercise_07()` | Tính biệt thức rồi thay vào biểu thức; kiểm tra mẫu khác 0 và căn bậc hai có nghĩa trong số thực. |
| 08 | `exercise_08()` | Dùng `**` để tính lũy thừa, `abs()` để lấy trị tuyệt đối. |
| 09 | `exercise_09()` | `int()` bỏ phần thập phân về phía 0, ví dụ `-3.7` thành `-3`. |
| 10 | `exercise_10()` | Nhập chuỗi, kiểm tra có đúng một ký tự rồi in ra. |
| 11 | `exercise_11()` | Vòng lặp từ 1 đến 10, nhân lần lượt với `n`. |
| 12 | `exercise_12()` | Diện tích = đáy × chiều cao / 2 = 30 cm². |
| 13 | `exercise_13()` | Kiểm tra đồng nhất thức tại ba góc tính bằng radian; dùng `isclose()` để xử lý sai số số thực. |

Chạy từ thư mục gốc:

```sh
docker compose run --rm python python exercise/homework/session_01/main.py
```

Nếu đã vào container, chạy `python exercise/homework/session_01/main.py`. Nếu đang ở thư mục session, chỉ cần `python main.py`.

Nhập số bài để chạy; kết thúc bài sẽ quay về menu. Nhập `0` để thoát. Nhập sai kiểu hoặc thiếu giá trị sẽ được báo lỗi và quay về menu.

Bài 01: nhập đơn giá `1000`, số lượng `2`, kết quả lần lượt là `2000`, `200`, `2200`.

Bài 02: nhập `5 10 9` được `8.0`; nhập `3 9 8` được `6.7` khi làm tròn một chữ số thập phân. Ví dụ `6.6` trong đề không khớp quy tắc làm tròn thông thường vì `20 / 3 = 6.666...`.

Bài 06: ví dụ `-3 → -2 -4` trong đề đảo thứ tự so với ví dụ `5 → 4 6`. Lời giải thống nhất in số liền trước rồi số liền sau: `-3 → -4 -2`.

Các bài yêu cầu nhiều giá trị (trừ bài 01) nhập trên cùng một dòng, cách nhau bằng khoảng trắng. Giả sử người dùng nhập đúng kiểu và đủ số lượng; bài 03–04 giả sử đúng số chữ số như đề yêu cầu.

# Session 03 — Vòng lặp và danh sách

Đề bài: [Bài 3 — Cấu trúc lặp](../../../docs/bai_3_cau-truc-lap.md).

Toàn bộ 24 lời giải và menu nằm trong `main.py`, mỗi câu là một hàm `exercise_XX()`. Lời nhắc và kết quả trong chương trình dùng tiếng Anh.

## Chạy chương trình

Trong container, từ thư mục `/app`:

```sh
python exercise/homework/session_03/main.py
```

Hoặc chạy từ terminal trên máy tại thư mục gốc project:

```sh
docker compose run --rm python python exercise/homework/session_03/main.py
```

Nhập số câu từ `1` đến `24` để chạy. Kết thúc câu sẽ quay lại menu; nhập `0` tại menu để thoát. Các câu có số `0` làm dấu kết thúc chỉ kết thúc câu đang chạy. Các câu nhập nhiều số liên tiếp đọc mỗi số trên một dòng; câu 18–20 nhập danh sách trên một dòng, cách nhau bằng khoảng trắng.

## Cách giải

| Câu | Cách giải |
| --- | --- |
| 01 | Dùng `% 10` lấy từng chữ số, xét chẵn/lẻ, dùng `// 10` bỏ chữ số cuối. |
| 02 | Dùng `isqrt()` tìm căn nguyên; so sánh khoảng cách tới hai số chính phương kề nhau. Số âm có số chính phương gần nhất là 0. |
| 03 | Nhập lại bằng vòng lặp cho tới khi là số dương hữu hạn. |
| 04 | Kiểm tra riêng từng điểm trong khoảng 0–10, sau đó lấy trung bình. |
| 05 | Dùng `for` in từ 1 đến N. |
| 06 | Nhập lại tháng tới khi hợp lệ rồi rẽ nhánh chọn mùa. |
| 07 | Nhập lại mã thứ tới khi hợp lệ rồi lấy tên tiếng Anh. |
| 08 | Dùng biến lớn nhất ban đầu là `None`, cập nhật tới khi nhập 0; không đưa 0 kết thúc vào dãy. |
| 09 | Lặp nhập tử và mẫu, chia khi cả hai khác 0; dừng ngay khi một số bằng 0. |
| 10 | Tách và cộng từng chữ số bằng vòng lặp. |
| 11 | Đọc tới 0, chỉ cộng số dương. |
| 12 | Đọc tới 0, đếm số nguyên âm. |
| 13 | Tách từng chữ số, tăng bộ đếm nếu chữ số bằng 7. |
| 14 | Dùng `while` tính bốn tổng; cộng dồn mẫu tam giác cho tổng đầu. |
| 15 | Nhập N hợp lệ, duyệt N số và giữ số lẻ lớn nhất; nhập `c` để làm lại câu. |
| 16 | Duyệt từ 1 đến trị tuyệt đối của N, giữ số chia hết N. |
| 17 | Dùng `for` tính hai tổng. |
| 18 | Duyệt danh sách, giữ số chia hết cho 5 lớn nhất; xử lý khi không có. |
| 19 | Dùng `for` tạo danh sách mới chứa các số không lớn hơn A. |
| 20 | Dùng `for` tìm vị trí đầu tiên có giá trị lớn hơn hoặc bằng B, rồi `insert()`; nếu không có thì chèn cuối. |
| 21 | Dùng `while` tìm đủ N số nguyên tố, kết hợp `for` thử ước đến căn nguyên của ứng viên. |
| 22 | Khởi tạo `guess = x / 2`, cập nhật Newton tới khi sai số bình phương không quá `1e-12`; xử lý riêng x = 0. |
| 23 | Duyệt chuỗi nhị phân, cập nhật `decimal = decimal * 2 + digit`, kiểm tra chỉ chứa 0 và 1. |
| 24 | Cộng khoảng cách giữa các đỉnh liên tiếp, cuối cùng cộng cạnh từ đỉnh cuối về đỉnh đầu; in các đỉnh và chu vi. |

## Quy ước và điểm chưa rõ trong đề

- Câu 05 dùng N nguyên dương vì yêu cầu liệt kê các số nguyên từ 1 đến N.
- Câu 06 dùng mùa theo tháng: xuân 3–5, hè 6–8, thu 9–11, đông 12–2. Đề chưa quy định cách chia mùa.
- Câu 07 dùng `1 = Monday`, ..., `7 = Sunday`. Đề chỉ cho khoảng 1–7, chưa quy định cách ánh xạ.
- Câu 13 chỉ đọc một số nguyên dương theo mô tả. Số 0 trong ví dụ không phải số cần đếm; khi chạy menu có thể nhập 0 sau khi xong để thoát.
- Câu 14 tổng thứ tư và câu 17 tổng thứ hai lấy chỉ số từ 0 đến n, tức **n + 1 số hạng**, để đúng số hạng cuối `(2n + 1)/(2n + 2)` ghi trong đề. Với n = 1, tổng này bằng 1.25.
- Câu 16 in các **ước dương** của trị tuyệt đối N. N = 0 có vô số ước nguyên khác 0, nên in thông báo riêng.
- Câu 18–20 dùng danh sách số do người dùng nhập. Cho phép dòng trống biểu diễn danh sách rỗng. Câu 20 yêu cầu danh sách đã tăng dần và kiểm tra điều kiện trước khi chèn.
- Câu 22 xử lý số không âm hữu hạn; nếu số thực không cải thiện được nữa hoặc dao động giữa hai giá trị, in giá trị xấp xỉ kèm thông báo giới hạn độ chính xác thay vì lặp mãi. Tiêu chí sai số tuyệt đối trong đề cũng có thể cho kết quả kém chính xác tương đối khi x rất nhỏ.
- Câu 24 kết thúc khi x là dòng trống hoặc chỉ có khoảng trắng; cần ít nhất ba đỉnh. Không nhập lại đỉnh đầu ở cuối vì chương trình tự đóng đa giác.

## Ví dụ

- Câu 01: `12345` → 2 chữ số chẵn, 3 chữ số lẻ.
- Câu 02: `9` → `Yes`; `6` → 4; `8` → 9; `65` → 64.
- Câu 10: `307` → 10.
- Câu 11–12: nhập lần lượt `3`, `8`, `-2`, `7`, `-5`, `1`, `0` → tổng dương 19, có 2 số âm.
- Câu 21: `5` → `[2, 3, 5, 7, 11]`.
- Câu 24: các đỉnh `(0, 0)`, `(1, 0)`, `(0, 1)` → chu vi `3.414213562373`.
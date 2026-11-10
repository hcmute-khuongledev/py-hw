# Session 02 — Kiểu dữ liệu và cấu trúc rẽ nhánh

Đề bài: [bài 2](../../docs/bai_2_kieu-du-lieu_cau-truc-re-nhanh_HW.md).

| Bài | File | Cách giải |
| --- | --- | --- |
| 01 | `exercise_01.py` | Chuẩn hóa điểm chữ bằng `strip().upper()`, dùng `if/elif` ánh xạ sang điểm số; điểm không có trong bảng thì yêu cầu nhập lại. |
| 02 | `exercise_02.py` | Chấp nhận `0.0`, `0.4` hoặc số hữu hạn từ `0.6` trở lên; phân loại rồi tính thưởng bằng `2400 * rating`. |
| 03 | `exercise_03.py` | Năm nhuận nếu chia hết cho 400 hoặc chia hết cho 4 và không chia hết cho 100. |
| 04 | `exercise_04.py` | Nếu `a = 0`, xét phương trình bậc nhất hoặc hằng; ngược lại xét biệt thức âm, bằng 0, dương để giải trong tập số thực. |
| 05 | `exercise_05.py` | Kiểm tra `abs(number) < 10` cho từng số, thông báo nếu không có số phù hợp. |
| 06 | `exercise_06.py` | Dùng `max()` và `min()` cho năm số. |
| 07 | `exercise_07.py` | Thay năm vào công thức trong đề, dùng `//` cho phép chia lấy phần nguyên; ánh xạ mã 0–6 sang Chủ nhật–Thứ bảy. |
| 08 | `exercise_08.py` | Tháng hợp lệ khi `1 <= month <= 12`. |
| 09 | `exercise_09.py` | Rẽ nhánh theo `x > 0`; tại `x = 0` chọn nhánh thứ hai, được `-5`. |
| 10 | `exercise_10.py` | Duyệt năm số, tăng bộ đếm âm, dương hoặc bằng 0. |
| 11 | `exercise_11.py` | Dùng `% 2` để xét cả hai chẵn, chỉ một chẵn hoặc cả hai lẻ. |
| 12 | `exercise_12.py` | Với `b != 0`, kiểm tra `a % b == 0`; xử lý riêng `b = 0` để tránh chia dư cho 0. |
| 13 | `exercise_13.py` | Chỉ xét số dương, cập nhật giá trị nhỏ nhất; dùng `None` khi chưa tìm thấy. |
| 14 | `exercise_14.py` | Chỉ xét số chẵn, cập nhật giá trị lớn nhất; vẫn đúng khi tất cả các số chẵn đều âm. |
| 15 | `exercise_15.py` | Tìm số nằm giữa hai số còn lại bằng so sánh. |

## Chạy bài

Từ thư mục gốc, thay số bài trong đường dẫn:

```sh
docker compose run --rm python python exercises/session_02/exercise_01.py
docker compose run --rm python python exercises/session_02/exercise_02.py
```

Các bài nhiều số nhập trên một dòng, cách nhau bằng khoảng trắng. Ví dụ bài 04 nhập `1 -3 2`, bài 10 nhập `-1 0 2 -3 0`. Giả sử nhập đúng kiểu dữ liệu và đủ số lượng. Với giá trị không hợp lệ theo đề, chương trình in thông báo rồi kết thúc; chạy lại để nhập lần nữa.

## Một số trường hợp cần lưu ý

- Bài 01: `A+ → 4.0`, `a- → 3.7`, `F → 0.0`; `E` không hợp lệ.
- Bài 02: `0.4 → Acceptable Performance`, thưởng `$960.00`; `0.5` không hợp lệ; `0.8` hợp lệ, thưởng `$1920.00`.
- Bài 03: năm 2000 nhuận, 1900 không nhuận, 2024 nhuận.
- Bài 04: `1 -3 2` có nghiệm 2 và 1; `0 2 -4` có nghiệm 2; `0 0 0` có vô số nghiệm.
- Bài 12: quy ước `b = 0` được báo riêng, không thực hiện phép chia dư.
- Bài 15: đề không quy định các số trùng nhau. Lời giải hiểu “lớn nhì” là phần tử thứ hai khi xếp giảm dần và giữ giá trị trùng: `5 5 3 → 5`, `5 3 3 → 3`, `2 2 2 → 2`.

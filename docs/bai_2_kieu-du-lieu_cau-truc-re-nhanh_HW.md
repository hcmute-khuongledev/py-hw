# Danh Sách Bài Tập Lập Trình - Cấu Trúc Điều Kiện

### Bài 01

Viết chương trình đọc một ký tự từ bàn phím. Nếu ký tự được nhập là điểm chữ thì chuyển đổi thành điểm số như cách tính điểm ở một số trường đại học trên thế giới. Bảng ánh xạ có thể được thể hiện như hình bên:

Chương trình sẽ đọc ký tự từ người sử dụng. Sau đó, chương trình sẽ tính toán và hiển thị con số điểm tương ứng. Ngoài ra, chương trình có thể đưa ra thông báo “yêu cầu nhập lại” trong trường hợp người dùng nhập vào một ký tự không tồn tại trong bảng trên.

| Letter | Grade Points | 
| ----- | ----- | 
| A+ | 4.0 | 
| A | 4.0 | 
| A- | 3.7 | 
| B+ | 3.3 | 
| B | 3.0 | 
| B- | 2.7 | 
| C+ | 2.3 | 
| C | 2.0 | 
| C- | 1.7 | 
| D+ | 1.3 | 
| D | 1.0 | 
| F | 0 | 

### Bài 02

Viết chương trình đánh giá hiệu quả làm việc của nhân viên.

Một công ty muốn đánh giá hiệu quả làm việc của nhân viên công ty theo mỗi năm. Thang đo hiệu quả làm việc sẽ được đánh giá từ $0.0$ và giá trị càng cao thì thể hiện năng lực làm việc càng tốt của nhân viên. Giá trị đánh giá $n$ có thể là $0.0$, $0.4$ hoặc $0.6$ hoặc lớn hơn. Trong đó, các giá trị giữa $0.0$ và $0.4$ hoặc $0.4$ và $0.6$ thì không được sử dụng. Chi tiết được thể hiện trong bảng sau.

Giá trị thưởng cho mỗi nhân viên sau khi đánh giá sẽ tương ứng với công thức $\$2400 \times n$.

Hãy viết chương trình đọc vào giá trị $n$ từ người dùng và hãy chỉ ra rằng hiệu quả làm việc tương ứng của nhân viên có giá trị $n$ cho hiệu quả công việc là **unacceptable**, **acceptable** và **meritorious**. Nếu giá trị $n$ không thể hiện đúng như trong bảng thì đưa ra thông báo “vui lòng nhập lại”.

| Rating | Meaning | 
| ----- | ----- | 
| 0.0 | Unacceptable Performance | 
| 0.4 | Acceptable Performance | 
| 0.6 or more | Meritorious Performance | 

### Bài 03

Viết chương trình kiểm tra năm nhuận. Thông thường mỗi năm có khoảng 365 ngày. Tuy nhiên, thời gian này phụ thuộc vào thời gian Trái đất hoàn thành một vòng xoay quanh Mặt trời. Điều này dẫn đến có thể có thêm một ngày là ngày 29 tháng 2. Những năm có thêm ngày này được xem là năm nhuận. Cách tính năm nhuận sẽ được quyết định bởi một số điều sau:

* Số năm chia hết cho 400 là năm nhuận.

* Các năm còn lại:

  * Nếu chia hết cho 100 thì **không** là năm nhuận.

  * Nếu chia hết cho 4 thì **là** năm nhuận.

* Các trường hợp còn lại thì **không** là năm nhuận.

Hãy viết một chương trình đọc vào số năm từ người dùng và hiển thị thông báo chỉ ra rằng năm vừa nhập có phải là năm nhuận không?

### Bài 04

Viết code cho nhập ba số thực ($a, b, c$). Giải và biện luận nghiệm của phương trình bậc hai: $ax^2 + bx + c = 0$.

### Bài 05

Viết chương trình cho người dùng nhập ba số thực rồi tìm và in ra các số có trị tuyệt đối nhỏ hơn 10.

### Bài 06

Viết chương trình cho người dùng nhập 05 số thực rồi tìm max/min các số thực này.

### Bài 07

Viết chương trình xác định thứ trong tuần của ngày 1 tháng 1. Thứ trong tuần của ngày 1 tháng 1 đối với một năm được tính theo công thức sau:

$$
\text{day\_of\_the\_week} = (\text{year} + \lfloor(\text{year} - 1) / 4\rfloor - \lfloor(\text{year} - 1) / 100\rfloor + \lfloor(\text{year} - 1) / 400\rfloor) \pmod 7
$$

Kết quả của công thức trên là một số nguyên thể hiện thứ trong tuần. Việc mã hóa thứ sẽ bắt đầu với ngày Chủ nhật với số mã hóa là 0. Tương tự, ngày thứ Bảy sẽ có giá trị mã hóa là 6. Hãy sử dụng công thức trên và viết một chương trình đọc số năm từ người dùng. Chương trình sẽ tính toán và in ra thứ tương ứng đối với ngày 1 tháng 1 của năm mà người dùng nhập.

### Bài 08

Cho phép người dùng nhập vào một giá trị tháng. Hãy cho biết giá trị tháng vừa nhập có hợp lệ hay không?

Quy ước: tháng hợp lệ là tháng $\in [1, 12]$

### Bài 09

Cho phép người dùng nhập vào số thực $x$, xuất $f(x)$ theo công thức sau:

$$
f(x) = 
\begin{cases} 
x^2 + 3x + 5, & x > 0 \\
-x^2 - 3x - 5, & x \le 0 
\end{cases}
$$

### Bài 10

Cho phép người dùng nhập vào 5 số $a, b, c, d, e$. Hãy cho biết trong 5 số vừa nhập có bao nhiêu số âm, bao nhiêu số dương, bao nhiêu số bằng 0?

### Bài 11

Viết chương trình nhập vào 2 số nguyên dương $a, b$:

- Nếu cả $a$ và $b$ đều là số chẵn thì xuất câu: `"a va b la 2 so chan"`
- Nếu trong 2 số $a$ và $b$ chỉ có một số chẵn thì xuất ra câu: `"chi co mot so chan"`
- Nếu trong 2 số $a$ và $b$ không có số chẵn nào thì xuất ra câu: `"a, b la hai so le"`

### Bài 12

Cho phép người dùng nhập vào hai số nguyên $a, b$. Hãy cho biết số $a$ có phải là bội của số $b$ hay không?

| a | b | Kết quả | 
| ----- | ----- | ----- | 
| 8 | 2 | 8 la boi so cua 2 | 
| 8 | 3 | 8 la KHONG boi so cua 3 | 

### Bài 13

Nhập vào 3 số nguyên $a, b, c$. Xuất lên màn hình giá trị dương nhỏ nhất trong 3 số trên (nếu có).

| a | b | c | Kết quả | 
| ----- | ----- | ----- | ----- | 
| 8 | -24 | 9 | 8 | 
| -8 | 30 | 35 | 30 | 
| 8 | 3 | 9 | 3 | 
| 3 | 6 | 2 | 2 | 
| 4 | 0 | 1 | 1 | 

### Bài 14

Nhập vào 3 số nguyên tìm số chẵn lớn nhất.

### Bài 15

Nhập vào 3 số nguyên. Xuất lên màn hình số lớn nhì trong 3 số đó.

| a | b | c | Kết quả | 
| ----- | ----- | ----- | ----- | 
| 8 | 24 | 9 | 9 | 
| 8 | 30 | 35 | 30 | 
| 8 | 3 | 9 | 8 | 
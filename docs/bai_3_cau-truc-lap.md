# Danh Sách Bài Tập Lập Trình - Vòng Lặp & Danh Sách

### Bài 01

Nhập vào một số nguyên dương $N$ với $N \in [10000, 99999]$. Hãy cho biết trong số $N$ vừa nhập có bao nhiêu chữ số chẵn, bao nhiêu chữ số lẻ?

### Bài 02

Viết chương trình kiểm tra một số nguyên có phải SỐ CHÍNH PHƯƠNG không? Nếu không phải xuất SỐ CHÍNH PHƯƠNG gần nó nhất.

| input | output |
| :--- | :--- |
| 9 | Yes |
| 6 | 4 |
| 8 | 9 |
| 7 | 9 |
| 16 | Yes |
| 65 | 64 |

### Bài 03

Nhập vào số dương, nếu nhập sai nhập lại cho đến khi đúng, nếu nhập đúng thì xuất số đã nhập.

### Bài 04

Nhập điểm lý thuyết, thực hành; kiểm tra riêng từng điểm phải trong khoảng từ $[0 .. 10]$, nếu không đúng phải nhập lại cho đến khi nào hợp lệ thì xuất điểm trung bình cộng.

### Bài 05

Nhập vào 1 số dương, giả sử luôn nhập đúng, xuất các số từ 1 đến số đó.

**Ví dụ:** Nhap 5, Xuat `1 2 3 4 5`

### Bài 06

Nhập vào tháng trong năm, kiểm tra giá trị nhập phải hợp lệ (từ 1 đến 12) nếu sai yêu cầu nhập lại cho đúng. Khi đã nhập đúng thì xuất ra mùa của tháng đã nhập.

### Bài 07

Nhập vào thứ trong tuần, kiểm tra giá trị nhập phải hợp lệ (từ 1 đến 7) nếu sai yêu cầu nhập lại cho đúng. Khi đã nhập đúng thì xuất ra tên của thứ trong tuần là tiếng anh.

### Bài 08

Nhập vào lần lượt các số để tính ra giá trị lớn nhất, nếu nhập vào số 0 thì kết thúc việc nhập số. Xuất ra giá trị lớn nhất trong các số đã nhập.

### Bài 09

Nhập vào 2 số nguyên khác 0 là tử và mẫu của một phân số, xuất ra giá trị thập phân của phân số, ví dụ nhập tử là 5, nhập mẫu là 8 thì xuất ra giá trị phân số dạng thập phân là `0.625`, và cho nhập tiếp hai số khác để tính. Chương trình ngừng khi một trong hai số nhập vào là số 0.

### Bài 10

Nhập vào một số nguyên dương, kiểm tra nếu nhập không đúng phải nhập lại cho đúng. Tính tổng các chữ số trong số nguyên và xuất kết quả. (Ví dụ nhập 307 thì xuất tổng là 10)

### Bài 11

Nhập vào lần lượt các số và tính tổng các số dương, nếu nhập vào số 0 thì kết thúc việc nhập số. Xuất ra tổng các số dương.

**Ví dụ:** nhập `3 8 -2 7 -5 1 0`, dừng và xuất ra `19`

### Bài 12

Nhập vào các số nguyên hoặc nhập 0 để kết thúc. Đếm số lượng các số âm có trong dãy số vừa nhập.

**Ví dụ:** nhập `3 8 -2 7 -5 1 0`, dừng và xuất ra `"Co 2 so am"`

### Bài 13

Nhập vào một số nguyên dương. Đếm xem có bao nhiêu ký số 7 trong số vừa nhập.

**Ví dụ:** nhập `37577 0`, xuất ra `"Co 3 so 7"`

### Bài 14

Sử dụng vòng lặp `while` tính các tổng sau, với $n$ là một số nguyên dương nhập bởi người dùng:

$$
S(n) = 1 + \frac{1}{1 + 2} + \frac{1}{1 + 2 + 3} + \cdots + \frac{1}{1 + 2 + \cdots + n}
$$

$$
S(n) = \frac{1}{1 \times 2} + \frac{1}{2 \times 3} + \cdots + \frac{1}{n \times (n + 1)}
$$

$$
S(n) = \frac{1}{2} + \frac{2}{3} + \frac{3}{4} + \cdots + \frac{n}{n + 1}
$$

$$
S(n) = \frac{1}{2} + \frac{3}{4} + \frac{5}{6} + \cdots + \frac{2n + 1}{2n + 2}
$$

### Bài 15

Cho người dùng nhập số nguyên dương $N$. Nếu nhập sai thì cho nhập lại đến khi đúng. Sau đó cho người dùng nhập $N$ số nguyên và in ra số lẻ lớn nhất trong những số được nhập. Cuối cùng, hỏi người dùng có muốn tiếp tục không, nếu người dùng nhấn `'c'` thì tiếp tục, nhấn phím khác thì thoát chương trình.

### Bài 16

In ra tất cả ước số của một số nguyên $N$ nhập bởi người dùng.

### Bài 17

Dùng vòng lặp `for` tính các tổng sau, với $n$ nguyên dương nhập bởi người dùng:

$$
S(n) = \frac{1}{1 \times 2} + \frac{1}{2 \times 3} + \cdots + \frac{1}{n \times (n + 1)}
$$

$$
S(n) = \frac{1}{2} + \frac{3}{4} + \frac{5}{6} + \cdots + \frac{2n + 1}{2n + 2}
$$

### Bài 18

Tạo một list có độ dài tùy ý chứa các phần tử tùy ý. Dùng vòng lặp `for` tìm phần tử chia hết cho 5 lớn nhất.

### Bài 19

Tạo một list có độ dài tùy ý chứa các phần tử tùy ý. Dùng vòng lặp `for` xóa các phần tử lớn hơn $A$ trong list, với $A$ là một số thực nhập bởi người dùng.

**Gợi ý:** Có thể tạo list mới chứa phần tử không bị xóa. Nếu muốn xóa bằng lệnh `del` thì cần dùng vòng lặp `while`.

### Bài 20

Tạo một list có độ dài tùy ý chứa các phần tử đã sắp tăng dần. Dùng vòng lặp `for` chèn một số $B$ vào list sao cho list vẫn tăng dần, với $B$ là một số thực nhập bởi người dùng.

**Gợi ý:** dùng vòng lặp tìm ra vị trí (index) thích hợp cần chèn, sau đó dùng hàm `insert()` để chèn $B$ vào list. Có thể tìm hiểu từ khóa `break` trong vòng lặp để sử dụng.

### Bài 21

Tìm $N$ số nguyên tố đầu tiên và lưu vào 1 list. $N$ là một số nguyên dương nhập bởi người dùng.

**Yêu cầu:** dùng vòng lặp `for` kết hợp với vòng lặp `while`.

### Bài 22

Viết chương trình tính căn bậc hai của một số $x$. Sử dụng phương pháp Newton để tính toán và hiển thị căn bậc hai của một số $x$ được nhập bởi người dùng. Thuật toán Newton như sau:

* *Đọc số $x$ từ bàn phím*
* *Khởi tạo `guess` bằng $x/2$*
* *While `guess` không thỏa điều kiện do*
* Cập nhật giá trị `guess` bằng với trung bình của `guess` và $x/\text{guess}$.

Khi thuật toán chạy hoàn chỉnh thì `guess` chứa một giá trị xấp xỉ với căn bậc hai của $x$, giá trị của phép xấp xỉ sẽ phụ thuộc vào điều kiện thỏa mãn mà người dùng đặt. Trong bài tập này thì `guess` được xem là thỏa mãn khi giá trị tuyệt đối của $\text{guess} \times \text{guess}$ so với $x$ nhỏ hơn hoặc bằng $10^{-12}$.

### Bài 23

Viết chương trình thực hiện chuyển đổi một số nhị phân (binary) sang hệ thập phân (decimal). Chương trình sẽ đọc một chuỗi các số nhị phân. Sau đó, chương trình sẽ tính toán một số hệ thập phân tương đương. Cuối cùng, chương trình sẽ hiển thị số thập phân tương ứng lên màn hình.

### Bài 24

Viết chương trình tính chu vi của một đa giác. Chương trình sẽ đọc các tọa độ $x, y$ của các điểm trong một đa giác. Các tọa độ được đọc liên tục cho đến khi người sử dụng nhập khoảng trắng `( )` đối với tọa độ $x$. Mỗi khi đọc 1 tọa độ mới, chương trình sẽ tính toán khoảng cách của điểm mới nhập so với điểm trước đó. Khi nhập khoảng trắng vào trong tọa độ $x$ thì chương trình sẽ thêm khoảng cách từ điểm cuối đến điểm đầu để tính chu vi. Khi tính toán và hiển thị chu vi thì các tọa độ của mỗi điểm đã nhập cũng được hiển thị trên màn hình. Ví dụ có dạng như sau:

```text
Enter the first x-coordinate: 0
Enter the first y-coordinate: 0
Enter the next x-coordinate (blank to quit): 1
Enter the next y-coordinate: 0
Enter the next x-coordinate (blank to quit): 0
Enter the next y-coordinate: 1
Enter the next x-coordinate (blank to quit):
The perimeter of that polygon is 3.414213562373
```

### Bài 25

Parity bit là một cơ chế đơn giản để phát hiện các lỗi trong việc truyền dữ liệu thông qua một đường truyền không đáng tin cậy như đường dây điện thoại. Ý tưởng rất đơn giản đó là một bit sẽ được thêm vào và truyền đi sau mỗi một nhóm 8-bit dữ liệu. Vì thế một bit lỗi trên đường truyền có thể được phát hiện dễ dàng. Bit parity có thể được tính toán cho cả trường hợp parity là chẵn hoặc lẻ. Nếu là parity chẵn thì tổng số bit 1 được truyền, gồm 8 bit dữ liệu và 1 bit parity phải là số chẵn. Ngược lại, khi chọn bit parity lẻ thì tổng số bit 1 truyền đi sẽ là lẻ.

Viết chương trình tính bit parity của một nhóm 8 bit nhị phân được nhập bởi người dùng sử dụng parity chẵn. Chương trình sẽ đọc chuỗi nhị phân gồm 8 bit cho đến khi nhập khoảng trắng. Sau mỗi chuỗi được nhập vào bởi người dùng, chương trình cần hiển thị một thông điệp chỉ ra rằng người dùng muốn tính parity chẵn hay lẻ. Một thông điệp cảnh báo sẽ được hiển thị nếu người dùng nhập một chuỗi nhị phân có hơn 8 bit.

### Bài 26

Viết chương trình thực hiện chuyển đổi số thập phân thành nhị phân. Với số nguyên thập phân do người dùng nhập vào từ bàn phím hãy sử dụng phép chia được minh họa sau đây để thực hiện việc chuyển đổi. Khi chương trình chuyển đổi được hoàn tất, kết quả in ra màn hình sẽ chứa một chuỗi các bit nhị phân tương ứng với số thập phân mà người dùng nhập.

```text
Ban đầu cho chuỗi rỗng result
Cho q là thể hiện của số cần chuyển đổi
Repeat
    Cho r bằng với phần dư của phép chia q với 2
    Chuyển r thành chuỗi và cộng r với phần bắt đầu của result
    Thực hiện chia q với 2, loại bỏ phần dư, và lưu phần nguyên của phép chia vào chính q
Until q bằng 0
```
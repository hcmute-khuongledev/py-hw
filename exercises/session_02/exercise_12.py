"""Check whether a is a multiple of b, guarding division by zero."""


def main() -> None:
    a, b = map(int, input("Nhap 2 so nguyen a b: ").split())
    if b == 0:
        print("Khong the kiem tra bang phep chia du khi b = 0.")
    elif a % b == 0:
        print(f"{a} la boi so cua {b}")
    else:
        print(f"{a} la KHONG boi so cua {b}")


if __name__ == "__main__":
    main()

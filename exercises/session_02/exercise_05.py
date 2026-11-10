"""Print the inputs whose absolute values are less than 10."""


def main() -> None:
    a, b, c = map(float, input("Nhap 3 so thuc: ").split())
    found = False
    for number in (a, b, c):
        if abs(number) < 10:
            print(f"{number:g}")
            found = True
    if not found:
        print("Khong co so nao co tri tuyet doi nho hon 10.")


if __name__ == "__main__":
    main()

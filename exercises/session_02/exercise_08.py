"""Validate a month number."""


def main() -> None:
    month = int(input("Nhap thang: "))
    if 1 <= month <= 12:
        print("Thang hop le.")
    else:
        print("Thang khong hop le.")


if __name__ == "__main__":
    main()

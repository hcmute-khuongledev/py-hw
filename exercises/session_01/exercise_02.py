"""Calculate the arithmetic mean of three integers."""


def main() -> None:
    first, second, third = map(int, input("Nhap 3 so nguyen, cach nhau bang dau cach: ").split())
    average = (first + second + third) / 3
    print(f"Gia tri trung binh: {average:.1f}")


if __name__ == "__main__":
    main()

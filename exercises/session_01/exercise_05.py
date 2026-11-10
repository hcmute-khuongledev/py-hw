"""Swap two integers."""


def main() -> None:
    first, second = map(int, input("Nhap 2 so nguyen: ").split())
    first, second = second, first
    print(first, second)


if __name__ == "__main__":
    main()

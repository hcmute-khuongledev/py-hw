"""Find the middle value of three integers, retaining duplicates."""


def main() -> None:
    a, b, c = map(int, input("Nhap 3 so nguyen: ").split())
    if (a <= b <= c) or (c <= b <= a):
        second_largest = b
    elif (b <= a <= c) or (c <= a <= b):
        second_largest = a
    else:
        second_largest = c
    print(second_largest)


if __name__ == "__main__":
    main()

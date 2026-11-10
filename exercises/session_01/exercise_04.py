"""Calculate a five-digit license plate score."""


def main() -> None:
    number = int(input("Nhap so xe gom 5 chu so: "))
    digit_sum = (number // 10000 + number // 1000 % 10
                 + number // 100 % 10 + number // 10 % 10 + number % 10)
    print(digit_sum % 10)


if __name__ == "__main__":
    main()

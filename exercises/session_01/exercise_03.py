"""Calculate the mean of the digits of a three-digit integer."""


def main() -> None:
    number = abs(int(input("Nhap so nguyen co 3 chu so: ")))
    hundreds = number // 100
    tens = number // 10 % 10
    units = number % 10
    print(f"{(hundreds + tens + units) / 3:.2f}")


if __name__ == "__main__":
    main()

"""Check whether a Gregorian calendar year is a leap year."""


def main() -> None:
    year = int(input("Nhap nam duong lich: "))
    if year <= 0:
        print("Nam phai la so nguyen duong.")
    elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} la nam nhuan.")
    else:
        print(f"{year} khong la nam nhuan.")


if __name__ == "__main__":
    main()

"""Check whether a Gregorian calendar year is a leap year."""


def main() -> None:
    year = int(input("Enter a Gregorian calendar year: "))
    if year <= 0:
        print("The year must be a positive integer.")
    elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


if __name__ == "__main__":
    main()

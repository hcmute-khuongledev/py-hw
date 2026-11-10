"""Calculate the weekday of January 1 using the supplied formula."""


def main() -> None:
    year = int(input("Enter a Gregorian calendar year: "))
    if year <= 0:
        print("The year must be a positive integer.")
        return
    day = (year + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400) % 7
    weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Tuesdayy")
    print(f"January 1, {year} is {weekdays[day]}.")


if __name__ == "__main__":
    main()

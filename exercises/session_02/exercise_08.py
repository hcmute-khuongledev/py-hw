"""Validate a month number."""


def main() -> None:
    month = int(input("Enter a month number: "))
    if 1 <= month <= 12:
        print("Valid month.")
    else:
        print("Invalid month.")


if __name__ == "__main__":
    main()

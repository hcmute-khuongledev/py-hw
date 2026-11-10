"""Classify the parity of two positive integers."""


def main() -> None:
    a, b = map(int, input("Enter two positive integers a and b separated by spaces: ").split())
    if a <= 0 or b <= 0:
        print("Please enter two positive integers.")
    elif a % 2 == 0 and b % 2 == 0:
        print("Both a and b are even.")
    elif a % 2 == 0 or b % 2 == 0:
        print("Exactly one number is even.")
    else:
        print("Both a and b are odd.")


if __name__ == "__main__":
    main()

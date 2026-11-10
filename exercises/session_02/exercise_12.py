"""Check whether a is a multiple of b, guarding division by zero."""


def main() -> None:
    a, b = map(int, input("Enter two integers a and b separated by spaces: ").split())
    if b == 0:
        print("Cannot check using the modulo operator when b is zero.")
    elif a % b == 0:
        print(f"{a} is a multiple of {b}")
    else:
        print(f"{a} is NOT a multiple of {b}")


if __name__ == "__main__":
    main()

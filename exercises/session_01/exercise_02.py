"""Calculate the arithmetic mean of three integers."""


def main() -> None:
    first, second, third = map(int, input("Enter three integers separated by spaces: ").split())
    average = (first + second + third) / 3
    print(f"Average: {average:.1f}")


if __name__ == "__main__":
    main()

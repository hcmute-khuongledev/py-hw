"""Swap two integers."""


def main() -> None:
    first, second = map(int, input("Enter two integers separated by spaces: ").split())
    first, second = second, first
    print(first, second)


if __name__ == "__main__":
    main()

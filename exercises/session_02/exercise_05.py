"""Print the inputs whose absolute values are less than 10."""


def main() -> None:
    a, b, c = map(float, input("Enter three real numbers separated by spaces: ").split())
    found = False
    for number in (a, b, c):
        if abs(number) < 10:
            print(f"{number:g}")
            found = True
    if not found:
        print("No input has an absolute value less than 10.")


if __name__ == "__main__":
    main()

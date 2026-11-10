"""Find the largest and smallest of five real numbers."""


def main() -> None:
    a, b, c, d, e = map(float, input("Enter five real numbers separated by spaces: ").split())
    print(f"Max: {max(a, b, c, d, e):g}")
    print(f"Min: {min(a, b, c, d, e):g}")


if __name__ == "__main__":
    main()

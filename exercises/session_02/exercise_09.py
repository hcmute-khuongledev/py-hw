"""Evaluate a piecewise quadratic function."""


def main() -> None:
    x = float(input("Nhap so thuc x: "))
    if x > 0:
        result = x**2 + 3 * x + 5
    else:
        result = -x**2 - 3 * x - 5
    print(f"f(x) = {result:g}")


if __name__ == "__main__":
    main()

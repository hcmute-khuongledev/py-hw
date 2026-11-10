"""Evaluate (-b + sqrt(b**2 - 4*a*c)) / (2*a) over real numbers."""

from math import sqrt


def main() -> None:
    a, b, c = map(float, input("Enter a, b, and c separated by spaces: ").split())
    discriminant = b**2 - 4 * a * c
    if a == 0:
        print("Undefined expression: a must not be zero.")
    elif discriminant < 0:
        print("The expression is undefined over the real numbers.")
    else:
        print((-b + sqrt(discriminant)) / (2 * a))


if __name__ == "__main__":
    main()

"""Solve a quadratic equation, including degenerate linear cases."""

from math import sqrt


def main() -> None:
    a, b, c = map(float, input("Enter a, b, and c separated by spaces: ").split())
    if a == 0:
        if b != 0:
            print(f"Linear equation, x = {-c / b:g}")
        elif c == 0:
            print("The equation has infinitely many solutions.")
        else:
            print("The equation has no solutions.")
        return

    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        print("The equation has no real solutions.")
    elif discriminant == 0:
        print(f"Repeated root: x = {-b / (2 * a):g}")
    else:
        first_root = (-b + sqrt(discriminant)) / (2 * a)
        second_root = (-b - sqrt(discriminant)) / (2 * a)
        print(f"x1 = {first_root:g}; x2 = {second_root:g}")


if __name__ == "__main__":
    main()

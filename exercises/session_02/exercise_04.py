"""Solve a quadratic equation, including degenerate linear cases."""

from math import sqrt


def main() -> None:
    a, b, c = map(float, input("Nhap a b c: ").split())
    if a == 0:
        if b != 0:
            print(f"Phuong trinh bac nhat, x = {-c / b:g}")
        elif c == 0:
            print("Phuong trinh co vo so nghiem.")
        else:
            print("Phuong trinh vo nghiem.")
        return

    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        print("Phuong trinh vo nghiem trong tap so thuc.")
    elif discriminant == 0:
        print(f"Nghiem kep: x = {-b / (2 * a):g}")
    else:
        first_root = (-b + sqrt(discriminant)) / (2 * a)
        second_root = (-b - sqrt(discriminant)) / (2 * a)
        print(f"x1 = {first_root:g}; x2 = {second_root:g}")


if __name__ == "__main__":
    main()

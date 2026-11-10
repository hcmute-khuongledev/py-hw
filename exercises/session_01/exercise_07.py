"""Evaluate (-b + sqrt(b**2 - 4*a*c)) / (2*a) over real numbers."""

from math import sqrt


def main() -> None:
    a, b, c = map(float, input("Nhap a b c: ").split())
    discriminant = b**2 - 4 * a * c
    if a == 0:
        print("Bieu thuc khong xac dinh: a phai khac 0.")
    elif discriminant < 0:
        print("Bieu thuc khong xac dinh trong tap so thuc.")
    else:
        print((-b + sqrt(discriminant)) / (2 * a))


if __name__ == "__main__":
    main()

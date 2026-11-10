"""Classify the parity of two positive integers."""


def main() -> None:
    a, b = map(int, input("Nhap 2 so nguyen duong a b: ").split())
    if a <= 0 or b <= 0:
        print("Vui long nhap 2 so nguyen duong.")
    elif a % 2 == 0 and b % 2 == 0:
        print("a va b la 2 so chan")
    elif a % 2 == 0 or b % 2 == 0:
        print("chi co mot so chan")
    else:
        print("a, b la hai so le")


if __name__ == "__main__":
    main()

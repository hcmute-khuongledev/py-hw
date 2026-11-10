"""Calculate the subtotal, 10% tax, and total price."""

TAX_RATE = 0.10


def main() -> None:
    unit_price = float(input("Nhap don gia: "))
    quantity = int(input("Nhap so luong: "))

    subtotal = unit_price * quantity
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    print(f"Tong tien truoc thue: {unit_price:g}*{quantity}={subtotal:g}")
    print(f"Tien thue: {tax:g}")
    print(f"Tong tien sau thue: {total:g}")


if __name__ == "__main__":
    main()

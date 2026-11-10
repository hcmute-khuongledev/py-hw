"""Calculate the subtotal, 10% tax, and total price."""

TAX_RATE = 0.10


def main() -> None:
    unit_price = float(input("Enter unit price: "))
    quantity = int(input("Enter quantity: "))

    subtotal = unit_price * quantity
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    print(f"Subtotal: {unit_price:g}*{quantity}={subtotal:g}")
    print(f"Tax: {tax:g}")
    print(f"Total including tax: {total:g}")


if __name__ == "__main__":
    main()

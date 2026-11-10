"""Classify employee performance and calculate the bonus."""

from math import isfinite

BONUS_BASE = 2400


def main() -> None:
    rating = float(input("Nhap gia tri danh gia: "))
    if not isfinite(rating):
        print("Vui long nhap lai.")
        return
    if rating == 0.0:
        meaning = "Unacceptable Performance"
    elif rating == 0.4:
        meaning = "Acceptable Performance"
    elif rating >= 0.6:
        meaning = "Meritorious Performance"
    else:
        print("Vui long nhap lai.")
        return
    print(meaning)
    print(f"Tien thuong: ${BONUS_BASE * rating:.2f}")


if __name__ == "__main__":
    main()

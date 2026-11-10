"""Classify employee performance and calculate the bonus."""

from math import isfinite

BONUS_BASE = 2400


def main() -> None:
    rating = float(input("Enter a performance rating: "))
    if not isfinite(rating):
        print("Invalid rating. Please enter 0.0, 0.4, or a finite value of at least 0.6.")
        return
    if rating == 0.0:
        meaning = "Unacceptable Performance"
    elif rating == 0.4:
        meaning = "Acceptable Performance"
    elif rating >= 0.6:
        meaning = "Meritorious Performance"
    else:
        print("Invalid rating. Please enter 0.0, 0.4, or a finite value of at least 0.6.")
        return
    print(meaning)
    print(f"Bonus: ${BONUS_BASE * rating:.2f}")


if __name__ == "__main__":
    main()

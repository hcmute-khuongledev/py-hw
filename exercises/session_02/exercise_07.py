"""Calculate the weekday of January 1 using the supplied formula."""


def main() -> None:
    year = int(input("Nhap nam duong lich: "))
    if year <= 0:
        print("Nam phai la so nguyen duong.")
        return
    day = (year + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400) % 7
    weekdays = ("Chu nhat", "Thu hai", "Thu ba", "Thu tu", "Thu nam", "Thu sau", "Thu bay")
    print(f"Ngay 01/01/{year} la {weekdays[day]}.")


if __name__ == "__main__":
    main()

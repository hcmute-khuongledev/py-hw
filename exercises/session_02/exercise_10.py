"""Count negative, positive, and zero inputs."""


def main() -> None:
    a, b, c, d, e = map(float, input("Nhap 5 so: ").split())
    negative_count = positive_count = zero_count = 0
    for number in (a, b, c, d, e):
        if number < 0:
            negative_count += 1
        elif number > 0:
            positive_count += 1
        else:
            zero_count += 1
    print(f"So am: {negative_count}")
    print(f"So duong: {positive_count}")
    print(f"So bang 0: {zero_count}")


if __name__ == "__main__":
    main()

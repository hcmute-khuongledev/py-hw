"""Find the largest even integer among three inputs."""


def main() -> None:
    a, b, c = map(int, input("Nhap 3 so nguyen: ").split())
    largest = None
    for number in (a, b, c):
        if number % 2 == 0 and (largest is None or number > largest):
            largest = number
    if largest is None:
        print("Khong co so chan.")
    else:
        print(largest)


if __name__ == "__main__":
    main()

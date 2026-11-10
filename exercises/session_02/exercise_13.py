"""Find the smallest positive integer among three inputs."""


def main() -> None:
    a, b, c = map(int, input("Nhap 3 so nguyen: ").split())
    smallest = None
    for number in (a, b, c):
        if number > 0 and (smallest is None or number < smallest):
            smallest = number
    if smallest is None:
        print("Khong co so duong.")
    else:
        print(smallest)


if __name__ == "__main__":
    main()

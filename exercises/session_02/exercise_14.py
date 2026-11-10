"""Find the largest even integer among three inputs."""


def main() -> None:
    a, b, c = map(int, input("Enter three integers separated by spaces: ").split())
    largest = None
    for number in (a, b, c):
        if number % 2 == 0 and (largest is None or number > largest):
            largest = number
    if largest is None:
        print("No even numbers found.")
    else:
        print(largest)


if __name__ == "__main__":
    main()

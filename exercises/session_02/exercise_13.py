"""Find the smallest positive integer among three inputs."""


def main() -> None:
    a, b, c = map(int, input("Enter three integers separated by spaces: ").split())
    smallest = None
    for number in (a, b, c):
        if number > 0 and (smallest is None or number < smallest):
            smallest = number
    if smallest is None:
        print("No positive numbers found.")
    else:
        print(smallest)


if __name__ == "__main__":
    main()

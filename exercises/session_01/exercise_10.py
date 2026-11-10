"""Read and print a single character."""


def main() -> None:
    character = input("Enter one character: ")
    if len(character) == 1:
        print(character)
    else:
        print("Please enter exactly one character.")


if __name__ == "__main__":
    main()

"""Read and print a single character."""


def main() -> None:
    character = input("Nhap mot ky tu: ")
    if len(character) == 1:
        print(character)
    else:
        print("Vui long nhap dung mot ky tu.")


if __name__ == "__main__":
    main()

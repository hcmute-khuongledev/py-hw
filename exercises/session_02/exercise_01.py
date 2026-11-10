"""Convert a letter grade to grade points using conditional statements."""


def main() -> None:
    grade = input("Enter a letter grade: ").strip().upper()
    if grade == "A+" or grade == "A":
        points = 4.0
    elif grade == "A-":
        points = 3.7
    elif grade == "B+":
        points = 3.3
    elif grade == "B":
        points = 3.0
    elif grade == "B-":
        points = 2.7
    elif grade == "C+":
        points = 2.3
    elif grade == "C":
        points = 2.0
    elif grade == "C-":
        points = 1.7
    elif grade == "D+":
        points = 1.3
    elif grade == "D":
        points = 1.0
    elif grade == "F":
        points = 0.0
    else:
        print("Invalid grade. Please enter a valid letter grade.")
        return
    print(f"Grade points: {points:.1f}")


if __name__ == "__main__":
    main()

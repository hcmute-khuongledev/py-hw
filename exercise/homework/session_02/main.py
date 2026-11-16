"""Homework solutions and an interactive session menu."""


from math import isfinite
from math import sqrt


BONUS_BASE = 2400


def exercise_01() -> None:
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


def exercise_02() -> None:
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


def exercise_03() -> None:
    year = int(input("Enter a Gregorian calendar year: "))
    if year <= 0:
        print("The year must be a positive integer.")
    elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


def exercise_04() -> None:
    a, b, c = map(float, input("Enter a, b, and c separated by spaces: ").split())
    if a == 0:
        if b != 0:
            print(f"Linear equation, x = {-c / b:g}")
        elif c == 0:
            print("The equation has infinitely many solutions.")
        else:
            print("The equation has no solutions.")
        return

    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        print("The equation has no real solutions.")
    elif discriminant == 0:
        print(f"Repeated root: x = {-b / (2 * a):g}")
    else:
        first_root = (-b + sqrt(discriminant)) / (2 * a)
        second_root = (-b - sqrt(discriminant)) / (2 * a)
        print(f"x1 = {first_root:g}; x2 = {second_root:g}")


def exercise_05() -> None:
    a, b, c = map(float, input("Enter three real numbers separated by spaces: ").split())
    found = False
    for number in (a, b, c):
        if abs(number) < 10:
            print(f"{number:g}")
            found = True
    if not found:
        print("No input has an absolute value less than 10.")


def exercise_06() -> None:
    a, b, c, d, e = map(float, input("Enter five real numbers separated by spaces: ").split())
    print(f"Max: {max(a, b, c, d, e):g}")
    print(f"Min: {min(a, b, c, d, e):g}")


def exercise_07() -> None:
    year = int(input("Enter a Gregorian calendar year: "))
    if year <= 0:
        print("The year must be a positive integer.")
        return
    day = (year + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400) % 7
    days_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    print(f"January 1, {year} is {days_of_week[day]}.")


def exercise_08() -> None:
    month = int(input("Enter a month number: "))
    if 1 <= month <= 12:
        print("Valid month.")
    else:
        print("Invalid month.")


def exercise_09() -> None:
    x = float(input("Enter real number x: "))
    if x > 0:
        result = x**2 + 3 * x + 5
    else:
        result = -x**2 - 3 * x - 5
    print(f"f(x) = {result:g}")


def exercise_10() -> None:
    a, b, c, d, e = map(float, input("Enter five numbers separated by spaces: ").split())
    negative_count = positive_count = zero_count = 0
    for number in (a, b, c, d, e):
        if number < 0:
            negative_count += 1
        elif number > 0:
            positive_count += 1
        else:
            zero_count += 1
    print(f"Negative numbers: {negative_count}")
    print(f"Positive numbers: {positive_count}")
    print(f"Zeros: {zero_count}")


def exercise_11() -> None:
    a, b = map(int, input("Enter two positive integers a and b separated by spaces: ").split())
    if a <= 0 or b <= 0:
        print("Please enter two positive integers.")
    elif a % 2 == 0 and b % 2 == 0:
        print("Both a and b are even.")
    elif a % 2 == 0 or b % 2 == 0:
        print("Exactly one number is even.")
    else:
        print("Both a and b are odd.")


def exercise_12() -> None:
    a, b = map(int, input("Enter two integers a and b separated by spaces: ").split())
    if b == 0:
        print("Cannot check using the modulo operator when b is zero.")
    elif a % b == 0:
        print(f"{a} is a multiple of {b}")
    else:
        print(f"{a} is NOT a multiple of {b}")


def exercise_13() -> None:
    a, b, c = map(int, input("Enter three integers separated by spaces: ").split())
    smallest = None
    for number in (a, b, c):
        if number > 0 and (smallest is None or number < smallest):
            smallest = number
    if smallest is None:
        print("No positive numbers found.")
    else:
        print(smallest)


def exercise_14() -> None:
    a, b, c = map(int, input("Enter three integers separated by spaces: ").split())
    largest = None
    for number in (a, b, c):
        if number % 2 == 0 and (largest is None or number > largest):
            largest = number
    if largest is None:
        print("No even numbers found.")
    else:
        print(largest)


def exercise_15() -> None:
    a, b, c = map(int, input("Enter three integers separated by spaces: ").split())
    if (a <= b <= c) or (c <= b <= a):
        second_largest = b
    elif (b <= a <= c) or (c <= a <= b):
        second_largest = a
    else:
        second_largest = c
    print(second_largest)


EXERCISES = {
    "1": ('Letter grade conversion', exercise_01),
    "2": ('Employee performance and bonus', exercise_02),
    "3": ('Leap year', exercise_03),
    "4": ('Quadratic equation', exercise_04),
    "5": ('Absolute values less than 10', exercise_05),
    "6": ('Maximum and minimum', exercise_06),
    "7": ('Weekday of January 1', exercise_07),
    "8": ('Validate a month', exercise_08),
    "9": ('Piecewise function', exercise_09),
    "10": ('Count negative, positive, and zero values', exercise_10),
    "11": ('Even and odd integers', exercise_11),
    "12": ('Check a multiple', exercise_12),
    "13": ('Smallest positive integer', exercise_13),
    "14": ('Largest even integer', exercise_14),
    "15": ('Second largest integer', exercise_15),
}


def main() -> None:
    while True:
        print("\nSession 02 - Homework")
        for number, (title, _) in EXERCISES.items():
            print(f"{number:>2}. {title}")
        print(" 0. Exit")

        try:
            choice = input("Choose an exercise: ").strip()
            if choice == "0":
                print("Goodbye!")
                return
            if choice not in EXERCISES:
                print("Invalid choice. Please select a number from the menu.")
                continue

            title, exercise = EXERCISES[choice]
            print(f"\n--- {title} ---")
            try:
                exercise()
            except ValueError:
                print("Invalid input. Please enter the required number and type of values.")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return


if __name__ == "__main__":
    main()

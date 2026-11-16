"""Homework solutions and an interactive session menu."""


from math import sqrt
from math import cos, isclose, pi, sin


TAX_RATE = 0.10


def exercise_01() -> None:
    unit_price = float(input("Enter unit price: "))
    quantity = int(input("Enter quantity: "))

    subtotal = unit_price * quantity
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    print(f"Subtotal: {unit_price:g}*{quantity}={subtotal:g}")
    print(f"Tax: {tax:g}")
    print(f"Total including tax: {total:g}")


def exercise_02() -> None:
    first, second, third = map(int, input("Enter three integers separated by spaces: ").split())
    average = (first + second + third) / 3
    print(f"Average: {average:.1f}")


def exercise_03() -> None:
    number = abs(int(input("Enter a three-digit integer: ")))
    hundreds = number // 100
    tens = number // 10 % 10
    units = number % 10
    print(f"{(hundreds + tens + units) / 3:.2f}")


def exercise_04() -> None:
    number = int(input("Enter a five-digit license plate number: "))
    digit_sum = (number // 10000 + number // 1000 % 10
                 + number // 100 % 10 + number // 10 % 10 + number % 10)
    print(digit_sum % 10)


def exercise_05() -> None:
    first, second = map(int, input("Enter two integers separated by spaces: ").split())
    first, second = second, first
    print(first, second)


def exercise_06() -> None:
    number = int(input("Enter integer k: "))
    print(number - 1, number + 1)


def exercise_07() -> None:
    a, b, c = map(float, input("Enter a, b, and c separated by spaces: ").split())
    discriminant = b**2 - 4 * a * c
    if a == 0:
        print("Undefined expression: a must not be zero.")
    elif discriminant < 0:
        print("The expression is undefined over the real numbers.")
    else:
        print((-b + sqrt(discriminant)) / (2 * a))


def exercise_08() -> None:
    x = int(input("Enter integer x: "))
    print(x**8 - 5 + abs(x))


def exercise_09() -> None:
    number = float(input("Enter a real number: "))
    print(int(number))


def exercise_10() -> None:
    character = input("Enter one character: ")
    if len(character) == 1:
        print(character)
    else:
        print("Please enter exactly one character.")


def exercise_11() -> None:
    number = int(input("Enter integer n: "))
    for multiplier in range(1, 11):
        print(f"{number} x {multiplier} = {number * multiplier}")


def exercise_12() -> None:
    base = 10
    height = 6
    area = base * height / 2
    print(f"Triangle area: {area:g} cm^2")


def exercise_13() -> None:
    for label, x in [("pi", pi), ("pi/2", pi / 2), ("4*pi/3", 4 * pi / 3)]:
        result = sin(x)**2 + cos(x)**2
        print(f"x = {label}: {isclose(result, 1.0, rel_tol=1e-9, abs_tol=1e-9)}")


EXERCISES = {
    "1": ('Price and tax', exercise_01),
    "2": ('Average of three integers', exercise_02),
    "3": ('Average of three digits', exercise_03),
    "4": ('License plate score', exercise_04),
    "5": ('Swap two integers', exercise_05),
    "6": ('Predecessor and successor', exercise_06),
    "7": ('Quadratic expression', exercise_07),
    "8": ('Power and absolute value', exercise_08),
    "9": ('Integer part', exercise_09),
    "10": ('Print a character', exercise_10),
    "11": ('Multiplication table', exercise_11),
    "12": ('Triangle area', exercise_12),
    "13": ('Trigonometric identity', exercise_13),
}


def main() -> None:
    while True:
        print("\nSession 01 - Homework")
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

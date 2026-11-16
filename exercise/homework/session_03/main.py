"""Loop and list exercises with an interactive menu."""

from math import hypot, isfinite, isqrt


def read_integer(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt))
            if (minimum is None or value >= minimum) and (maximum is None or value <= maximum):
                return value
        except ValueError:
            pass
        print("Invalid integer. Please try again.")


def read_number(prompt, minimum=None, maximum=None, positive=False):
    while True:
        try:
            value = float(input(prompt))
            if (isfinite(value) and (not positive or value > 0)
                    and (minimum is None or value >= minimum)
                    and (maximum is None or value <= maximum)):
                return value
        except ValueError:
            pass
        print("Invalid number. Please try again.")


def exercise_01():
    number = read_integer("Enter a five-digit integer: ", 10000, 99999)
    even_count = odd_count = 0
    while number > 0:
        if number % 10 % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        number //= 10
    print(f"Even digits: {even_count}; odd digits: {odd_count}")


def exercise_02():
    number = read_integer("Enter an integer: ")
    if number < 0:
        print("Nearest perfect square: 0")
        return
    root = isqrt(number)
    lower = root * root
    upper = (root + 1) ** 2
    if lower == number:
        print("Yes")
    else:
        nearest = lower if number - lower <= upper - number else upper
        print(f"Nearest perfect square: {nearest}")


def exercise_03():
    number = read_number("Enter a positive number: ", positive=True)
    print(f"Number: {number:g}")


def exercise_04():
    theory = read_number("Enter theory score (0-10): ", 0, 10)
    practice = read_number("Enter practice score (0-10): ", 0, 10)
    print(f"Average: {(theory + practice) / 2:g}")


def exercise_05():
    number = read_integer("Enter a positive integer: ", 1)
    for value in range(1, number + 1):
        print(value, end=" " if value < number else "\n")


def exercise_06():
    month = read_integer("Enter month (1-12): ", 1, 12)
    if 3 <= month <= 5:
        season = "Spring"
    elif 6 <= month <= 8:
        season = "Summer"
    elif 9 <= month <= 11:
        season = "Autumn"
    else:
        season = "Winter"
    print(season)


def exercise_07():
    day = read_integer("Enter weekday (1=Monday, 7=Sunday): ", 1, 7)
    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    print(weekdays[day - 1])


def exercise_08():
    largest = None
    while True:
        number = read_number("Enter a number (0 to finish): ")
        if number == 0:
            break
        if largest is None or number > largest:
            largest = number
    if largest is None:
        print("No numbers entered.")
    else:
        print(f"Maximum: {largest:g}")


def exercise_09():
    while True:
        numerator = read_integer("Enter numerator (0 to finish): ")
        if numerator == 0:
            break
        denominator = read_integer("Enter denominator (0 to finish): ")
        if denominator == 0:
            break
        print(f"Decimal value: {numerator / denominator:g}")


def exercise_10():
    number = read_integer("Enter a positive integer: ", 1)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    print(f"Digit sum: {total}")


def exercise_11():
    total = 0.0
    while True:
        number = read_number("Enter a number (0 to finish): ")
        if number == 0:
            break
        if number > 0:
            total += number
    print(f"Positive sum: {total:g}")


def exercise_12():
    count = 0
    while True:
        number = read_integer("Enter an integer (0 to finish): ")
        if number == 0:
            break
        if number < 0:
            count += 1
    print(f"Negative numbers: {count}")


def exercise_13():
    number = read_integer("Enter a positive integer: ", 1)
    count = 0
    while number > 0:
        if number % 10 == 7:
            count += 1
        number //= 10
    print(f"Digits equal to 7: {count}")


def exercise_14():
    n = read_integer("Enter a positive integer n: ", 1)
    index = 1
    triangular = 0
    first = second = third = 0.0
    while index <= n:
        triangular += index
        first += 1 / triangular
        second += 1 / (index * (index + 1))
        third += index / (index + 1)
        index += 1
    fourth = 0.0
    index = 0
    while index <= n:
        fourth += (2 * index + 1) / (2 * index + 2)
        index += 1
    print(f"Sum 1: {first:.12g}")
    print(f"Sum 2: {second:.12g}")
    print(f"Sum 3: {third:.12g}")
    print(f"Sum 4: {fourth:.12g}")


def exercise_15():
    while True:
        count = read_integer("Enter a positive integer N: ", 1)
        largest_odd = None
        for index in range(count):
            number = read_integer(f"Enter integer {index + 1}: ")
            if number % 2 != 0 and (largest_odd is None or number > largest_odd):
                largest_odd = number
        if largest_odd is None:
            print("No odd numbers found.")
        else:
            print(f"Largest odd integer: {largest_odd}")
        if input("Enter 'c' to continue, any other key to return: ").strip().lower() != "c":
            break


def exercise_16():
    number = read_integer("Enter a nonzero integer N: ")
    if number == 0:
        print("Zero has infinitely many nonzero integer divisors.")
        return
    divisors = []
    for candidate in range(1, abs(number) + 1):
        if number % candidate == 0:
            divisors.append(candidate)
    print("Positive divisors:", *divisors)


def exercise_17():
    n = read_integer("Enter a positive integer n: ", 1)
    first = second = 0.0
    for index in range(1, n + 1):
        first += 1 / (index * (index + 1))
    for index in range(n + 1):
        second += (2 * index + 1) / (2 * index + 2)
    print(f"Sum 1: {first:.12g}")
    print(f"Sum 2: {second:.12g}")


def exercise_18():
    numbers = list(map(int, input("Enter integers separated by spaces (blank for empty): ").split()))
    largest = None
    for number in numbers:
        if number % 5 == 0 and (largest is None or number > largest):
            largest = number
    if largest is None:
        print("No multiples of 5 found.")
    else:
        print(f"Largest multiple of 5: {largest}")


def exercise_19():
    numbers = list(map(float, input("Enter numbers separated by spaces (blank for empty): ").split()))
    threshold = read_number("Enter threshold A: ")
    remaining = []
    for number in numbers:
        if number <= threshold:
            remaining.append(number)
    print("Remaining list:", remaining)


def exercise_20():
    numbers = list(map(float, input("Enter sorted numbers separated by spaces (blank for empty): ").split()))
    for index in range(1, len(numbers)):
        if numbers[index] < numbers[index - 1]:
            print("The input list must be sorted in ascending order.")
            return
    value = read_number("Enter number B to insert: ")
    position = len(numbers)
    for index in range(len(numbers)):
        if numbers[index] >= value:
            position = index
            break
    numbers.insert(position, value)
    print("Updated list:", numbers)


def exercise_21():
    count = read_integer("Enter a positive integer N: ", 1)
    primes = []
    candidate = 2
    while len(primes) < count:
        prime = True
        for divisor in range(2, isqrt(candidate) + 1):
            if candidate % divisor == 0:
                prime = False
                break
        if prime:
            primes.append(candidate)
        candidate += 1
    print("First primes:", primes)


def exercise_22():
    x = read_number("Enter a nonnegative number x: ", minimum=0)
    if x == 0:
        print("Square root: 0")
        return
    guess = x / 2
    if guess == 0:
        guess = 1.0
    tolerance = 1e-12
    previous_guess = None
    while abs(guess * guess - x) > tolerance:
        next_guess = (guess + x / guess) / 2
        # Float precision can prevent the absolute error from reaching the target.
        if next_guess == guess or next_guess == previous_guess:
            print(f"Approximate square root: {guess:.15g} (floating-point precision limit)")
            return
        previous_guess = guess
        guess = next_guess
    print(f"Square root: {guess:.15g}")


def exercise_23():
    binary = input("Enter a binary number: ").strip()
    if not binary:
        print("Please enter at least one binary digit.")
        return
    decimal = 0
    for digit in binary:
        if digit not in "01":
            print("Invalid binary number. Use only 0 and 1.")
            return
        decimal = decimal * 2 + int(digit)
    print(f"Decimal: {decimal}")


def exercise_24():
    points = []
    perimeter = 0.0
    while True:
        text = input("Enter x-coordinate (blank to finish): ").strip()
        if not text:
            break
        x = float(text)
        if not isfinite(x):
            print("The coordinate must be finite.")
            continue
        y = read_number("Enter y-coordinate: ")
        if points:
            perimeter += hypot(x - points[-1][0], y - points[-1][1])
        points.append((x, y))
    if len(points) < 3:
        print("A polygon needs at least three vertices.")
        return
    perimeter += hypot(points[-1][0] - points[0][0], points[-1][1] - points[0][1])
    print("Vertices:", points)
    print(f"Perimeter: {perimeter:.12f}")


def exercise_25():
    while True:
        binary = input("Enter 8 binary digits (blank to finish): ").strip()
        if not binary:
            return
        if len(binary) != 8 or any(bit not in "01" for bit in binary):
            print("Invalid data. Enter exactly 8 bits using only 0 and 1.")
            continue
        while True:
            parity = input("Choose parity: even or odd (Enter for even): ").strip().lower()
            if not parity:
                parity = "even"
            if parity in ("even", "odd"):
                break
            print("Invalid parity. Please enter even or odd.")
        ones = 0
        for bit in binary:
            if bit == "1":
                ones += 1
        parity_bit = ones % 2
        if parity == "odd":
            parity_bit = 1 - parity_bit
        print(f"Parity mode: {parity}")
        print(f"Parity bit: {parity_bit}")
        print(f"Transmitted bits: {binary}{parity_bit}")


def exercise_26():
    number = read_integer("Enter a nonnegative decimal integer: ", 0)
    quotient = number
    result = ""
    while True:
        remainder = quotient % 2
        result = str(remainder) + result
        quotient //= 2
        if quotient == 0:
            break
    print(f"Binary: {result}")


EXERCISES = {
    "1": ('Count even and odd digits', exercise_01),
    "2": ('Nearest perfect square', exercise_02),
    "3": ('Read a positive number', exercise_03),
    "4": ('Validate scores and calculate average', exercise_04),
    "5": ('Print integers from 1 to N', exercise_05),
    "6": ('Month and season', exercise_06),
    "7": ('Weekday name', exercise_07),
    "8": ('Maximum until zero', exercise_08),
    "9": ('Repeated fraction conversion', exercise_09),
    "10": ('Sum of digits', exercise_10),
    "11": ('Sum of positive numbers', exercise_11),
    "12": ('Count negative integers', exercise_12),
    "13": ('Count digits equal to 7', exercise_13),
    "14": ('Series sums using while', exercise_14),
    "15": ('Largest odd integer with repeat', exercise_15),
    "16": ('Divisors of an integer', exercise_16),
    "17": ('Series sums using for', exercise_17),
    "18": ('Largest multiple of 5 in a list', exercise_18),
    "19": ('Remove values greater than A', exercise_19),
    "20": ('Insert into a sorted list', exercise_20),
    "21": ('First N prime numbers', exercise_21),
    "22": ('Newton square root', exercise_22),
    "23": ('Binary to decimal', exercise_23),
    "24": ('Polygon perimeter', exercise_24),
    "25": ('Parity bit for 8-bit data', exercise_25),
    "26": ('Decimal to binary', exercise_26),
}


def main() -> None:
    while True:
        print("\nSession 03 - Homework")
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

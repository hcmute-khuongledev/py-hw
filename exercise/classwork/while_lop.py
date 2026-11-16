n = int(input("Enter a positive integer n: "))

while n <= 0:
    n = int(input("Please enter n > 0: "))

total = 0
i = 2

while i <= n:
    total += i
    i += 2

print(f"The sum of even numbers from 1 to {n} is: {total}")

result = 0

while True:
    n = int(input("Enter a positive integer (0 or negative to stop): "))

    if n <= 0:
        break

    divisor_sum = 0
    divisor = 1

    while divisor <= n // 2:
        if n % divisor == 0:
            divisor_sum += divisor
        divisor += 1

    if divisor_sum == n:
        result += n

print(f"The sum of perfect numbers is: {result}")

import math

def prime_factors(value):
    if value <= 1:
        return []

    result = []

    # Handle division by 2 first
    while value % 2 == 0:
        result.append(2)
        value //= 2

    # Now check for odd divisors
    limit = int(math.isqrt(value)) + 1
    for divisor in range(3, limit, 2):
        while value % divisor == 0:
            result.append(divisor)
            value //= divisor

    # If anything remains, it must be a prime
    if value > 2:
        result.append(value)

    return result

def start():
    try:
        num = int(input("Enter a whole number to find its prime factors: "))
        output = prime_factors(num)
        print(f"Prime factorization of {num}: {output}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    start()

import math

def fermat_factors(number):
    if number <= 0:
        return "Error: Input must be a positive integer."
    if number % 2 == 0:
        return [2, number // 2]

    x = math.isqrt(number)
    if x * x < number:
        x += 1

    diff = x * x - number
    while not is_square(diff):
        x += 1
        diff = x * x - number

    y = math.isqrt(diff)
    return [x - y, x + y]

def is_square(value):
    root = math.isqrt(value)
    return root * root == value

def run():
    try:
        num = int(input("Enter an odd positive integer to factor: "))
        result = fermat_factors(num)
        print(f"Factors of {num}: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    run()

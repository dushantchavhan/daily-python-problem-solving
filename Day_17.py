# Day 17 - Sum of digits of a number

def sum_of_digits(n):
    n = abs(n)  # handle negative numbers
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n //= 10

    return total


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
num1 = 1234
print("Sum of digits:", sum_of_digits(num1))

# Test Case 2
num2 = 987
print("Sum of digits:", sum_of_digits(num2))

# Test Case 3
num3 = 0
print("Sum of digits:", sum_of_digits(num3))

# Test Case 4
num4 = -456
print("Sum of digits:", sum_of_digits(num4))
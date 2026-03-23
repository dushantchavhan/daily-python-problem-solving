# Day 16 - Count digits in a number

def count_digits(n):
    if n == 0:
        return 1

    count = 0
    n = abs(n)  # handle negative numbers

    while n > 0:
        count += 1
        n //= 10

    return count


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
num1 = 12345
print("Digits:", count_digits(num1))

# Test Case 2
num2 = 7
print("Digits:", count_digits(num2))

# Test Case 3
num3 = 0
print("Digits:", count_digits(num3))

# Test Case 4
num4 = -9876
print("Digits:", count_digits(num4))
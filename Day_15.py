# Day 15 - Armstrong Number

def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = 0

    for digit in num_str:
        total += int(digit) ** power

    return total == n


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
num1 = 153
print(num1, "is Armstrong:", is_armstrong(num1))

# Test Case 2
num2 = 370
print(num2, "is Armstrong:", is_armstrong(num2))

# Test Case 3
num3 = 123
print(num3, "is Armstrong:", is_armstrong(num3))

# Test Case 4
num4 = 9474
print(num4, "is Armstrong:", is_armstrong(num4))
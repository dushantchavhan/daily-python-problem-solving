# Day 18 - Reverse a number

def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)

    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return sign * reversed_num


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
num1 = 1234
print("Reversed:", reverse_number(num1))

# Test Case 2
num2 = 987
print("Reversed:", reverse_number(num2))

# Test Case 3
num3 = 1000
print("Reversed:", reverse_number(num3))

# Test Case 4
num4 = -456
print("Reversed:", reverse_number(num4))
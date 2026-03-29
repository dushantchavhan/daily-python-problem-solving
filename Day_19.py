# Day 19 - Check if number is palindrome

def is_palindrome_number(n):
    original = n
    n = abs(n)

    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return original == reversed_num


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
num1 = 121
print(num1, "is palindrome:", is_palindrome_number(num1))

# Test Case 2
num2 = 123
print(num2, "is palindrome:", is_palindrome_number(num2))

# Test Case 3
num3 = 7
print(num3, "is palindrome:", is_palindrome_number(num3))

# Test Case 4
num4 = -121
print(num4, "is palindrome:", is_palindrome_number(num4))
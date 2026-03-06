# Day 4 - Factorial using Recursion
# Factorial of n = n * (n-1) * (n-2) ... * 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
num1 = 5
print("Factorial of", num1, "=", factorial(num1))

# Test Case 2
num2 = 0
print("Factorial of", num2, "=", factorial(num2))

# Test Case 3
num3 = 3
print("Factorial of", num3, "=", factorial(num3))

# Test Case 4
num4 = 7
print("Factorial of", num4, "=", factorial(num4))
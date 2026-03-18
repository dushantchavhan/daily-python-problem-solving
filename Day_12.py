# Day 12 - Check if a number is prime

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
num1 = 7
print(num1, "is prime:", is_prime(num1))

# Test Case 2
num2 = 10
print(num2, "is prime:", is_prime(num2))

# Test Case 3
num3 = 1
print(num3, "is prime:", is_prime(num3))

# Test Case 4
num4 = 13
print(num4, "is prime:", is_prime(num4))
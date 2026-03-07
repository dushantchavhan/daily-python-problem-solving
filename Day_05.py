# Day 5 - Fibonacci Sequence
# Each number is the sum of the previous two numbers

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        next_number = a + b
        a = b
        b = next_number


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
print("First 5 Fibonacci numbers:")
fibonacci(5)

print("\n")

# Test Case 2
print("First 10 Fibonacci numbers:")
fibonacci(10)

print("\n")

# Test Case 3
print("First 1 Fibonacci number:")
fibonacci(1)
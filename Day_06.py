# Day 6 - Find Largest Number in a List

def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
nums1 = [3, 7, 2, 9, 4]
print("Largest number:", find_largest(nums1))

# Test Case 2
nums2 = [10, 25, 5, 18, 30]
print("Largest number:", find_largest(nums2))

# Test Case 3
nums3 = [-5, -2, -10, -1]
print("Largest number:", find_largest(nums3))

# Test Case 4
nums4 = [100]
print("Largest number:", find_largest(nums4))
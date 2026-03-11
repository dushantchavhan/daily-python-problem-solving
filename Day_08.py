# Day 8 - Find Second Largest Number in a List

def find_second_largest(numbers):
    if len(numbers) < 2:
        return None

    largest = second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return None

    return second_largest


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
nums1 = [10, 20, 4, 45, 99]
print("Second Largest:", find_second_largest(nums1))

# Test Case 2
nums2 = [5, 5, 5, 5]
print("Second Largest:", find_second_largest(nums2))

# Test Case 3
nums3 = [7, 2]
print("Second Largest:", find_second_largest(nums3))

# Test Case 4
nums4 = [100]
print("Second Largest:", find_second_largest(nums4))
# Day 13 - Find Missing Number in Array

def find_missing_number(numbers, n):
    # expected sum of 1 to n
    expected_sum = n * (n + 1) // 2

    # actual sum of given numbers
    actual_sum = sum(numbers)

    return expected_sum - actual_sum


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
nums1 = [1, 2, 4, 5]
n1 = 5
print("Missing number:", find_missing_number(nums1, n1))

# Test Case 2
nums2 = [1, 3, 4, 5, 6]
n2 = 6
print("Missing number:", find_missing_number(nums2, n2))

# Test Case 3
nums3 = [2, 3, 1, 5]
n3 = 5
print("Missing number:", find_missing_number(nums3, n3))

# Test Case 4
nums4 = [1]
n4 = 2
print("Missing number:", find_missing_number(nums4, n4))
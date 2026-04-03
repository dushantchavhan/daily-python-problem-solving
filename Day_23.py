# Day 23 - Check if a list is sorted

def is_sorted(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
nums1 = [1, 2, 3, 4, 5]
print("Is sorted:", is_sorted(nums1))

# Test Case 2
nums2 = [5, 3, 2, 1]
print("Is sorted:", is_sorted(nums2))

# Test Case 3
nums3 = [1, 3, 2, 4]
print("Is sorted:", is_sorted(nums3))

# Test Case 4
nums4 = []
print("Is sorted:", is_sorted(nums4))
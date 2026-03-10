# Day 7 - Reverse a List

def reverse_list(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        # swap elements
        numbers[left], numbers[right] = numbers[right], numbers[left]

        left += 1
        right -= 1

    return numbers


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
nums1 = [1, 2, 3, 4, 5]
print("Reversed:", reverse_list(nums1))

# Test Case 2
nums2 = [10, 20, 30]
print("Reversed:", reverse_list(nums2))

# Test Case 3
nums3 = [7]
print("Reversed:", reverse_list(nums3))

# Test Case 4
nums4 = []
print("Reversed:", reverse_list(nums4))
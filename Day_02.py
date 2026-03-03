# Day 2 - Binary Search
# Practicing searching in a sorted array

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
nums1 = [1, 3, 5, 7, 9, 11]
target1 = 7
print("Test Case 1:", binary_search(nums1, target1))

# Test Case 2
nums2 = [2, 4, 6, 8, 10]
target2 = 6
print("Test Case 2:", binary_search(nums2, target2))

# Test Case 3 (element not present)
nums3 = [5, 10, 15, 20]
target3 = 13
print("Test Case 3:", binary_search(nums3, target3))

# Test Case 4 (single element)
nums4 = [100]
target4 = 100
print("Test Case 4:", binary_search(nums4, target4))

# Test Case 5 (empty list)
nums5 = []
target5 = 1
print("Test Case 5:", binary_search(nums5, target5))
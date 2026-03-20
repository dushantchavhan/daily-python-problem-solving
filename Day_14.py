# Day 14 - Linear Search

def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
nums1 = [10, 20, 30, 40, 50]
target1 = 30
print("Index:", linear_search(nums1, target1))

# Test Case 2
nums2 = [5, 15, 25, 35]
target2 = 100
print("Index:", linear_search(nums2, target2))

# Test Case 3
nums3 = [1]
target3 = 1
print("Index:", linear_search(nums3, target3))

# Test Case 4
nums4 = []
target4 = 10
print("Index:", linear_search(nums4, target4))
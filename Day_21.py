# Day 21 - Find maximum and minimum in a list

def find_max_min(numbers):
    if len(numbers) == 0:
        return None, None

    maximum = minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
nums1 = [3, 7, 2, 9, 4]
max_val, min_val = find_max_min(nums1)
print("Max:", max_val, "Min:", min_val)

# Test Case 2
nums2 = [10, 25, 5, 18, 30]
max_val, min_val = find_max_min(nums2)
print("Max:", max_val, "Min:", min_val)

# Test Case 3
nums3 = [-5, -2, -10, -1]
max_val, min_val = find_max_min(nums3)
print("Max:", max_val, "Min:", min_val)

# Test Case 4
nums4 = []
max_val, min_val = find_max_min(nums4)
print("Max:", max_val, "Min:", min_val)
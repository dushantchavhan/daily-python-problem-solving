# Day 9 - Remove duplicates from a list

def remove_duplicates(numbers):
    unique_list = []

    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)

    return unique_list


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
nums1 = [1, 2, 2, 3, 4, 4, 5]
print("Unique numbers:", remove_duplicates(nums1))

# Test Case 2
nums2 = [10, 10, 10, 20, 30]
print("Unique numbers:", remove_duplicates(nums2))

# Test Case 3
nums3 = [7, 8, 9]
print("Unique numbers:", remove_duplicates(nums3))

# Test Case 4
nums4 = []
print("Unique numbers:", remove_duplicates(nums4))
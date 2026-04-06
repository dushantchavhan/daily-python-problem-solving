# Day 24 - Count frequency of elements in a list

def count_frequency(numbers):
    freq = {}

    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
nums1 = [1, 2, 2, 3, 3, 3]
print("Frequency:", count_frequency(nums1))

# Test Case 2
nums2 = [10, 20, 10, 30]
print("Frequency:", count_frequency(nums2))

# Test Case 3
nums3 = [5, 5, 5, 5]
print("Frequency:", count_frequency(nums3))

# Test Case 4
nums4 = []
print("Frequency:", count_frequency(nums4))
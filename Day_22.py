# Day 22 - Find sum and average of elements in a list

def sum_and_average(numbers):
    if len(numbers) == 0:
        return 0, 0

    total = 0

    for num in numbers:
        total += num

    average = total / len(numbers)

    return total, average


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
nums1 = [1, 2, 3, 4, 5]
total, avg = sum_and_average(nums1)
print("Sum:", total, "Average:", avg)

# Test Case 2
nums2 = [10, 20, 30]
total, avg = sum_and_average(nums2)
print("Sum:", total, "Average:", avg)

# Test Case 3
nums3 = [7]
total, avg = sum_and_average(nums3)
print("Sum:", total, "Average:", avg)

# Test Case 4
nums4 = []
total, avg = sum_and_average(nums4)
print("Sum:", total, "Average:", avg)
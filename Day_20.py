# Day 20 - Count even and odd numbers in a list

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count


# -------------------------
# Test Cases
# -------------------------

# Test Case 1
nums1 = [1, 2, 3, 4, 5, 6]
even, odd = count_even_odd(nums1)
print("Even:", even, "Odd:", odd)

# Test Case 2
nums2 = [10, 15, 20, 25, 30]
even, odd = count_even_odd(nums2)
print("Even:", even, "Odd:", odd)

# Test Case 3
nums3 = [7, 9, 11]
even, odd = count_even_odd(nums3)
print("Even:", even, "Odd:", odd)

# Test Case 4
nums4 = []
even, odd = count_even_odd(nums4)
print("Even:", even, "Odd:", odd)
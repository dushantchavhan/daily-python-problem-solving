# Day 1 - Two Sum Problem
# Practicing basic array + dictionary concept

def two_sum(nums, target):
    num_dict = {}

    for i in range(len(nums)):
        current = nums[i]
        remaining = target - current

        if remaining in num_dict:
            return [num_dict[remaining], i]

        num_dict[current] = i

    return []


# Example test case
nums = [2, 7, 11, 15]

target = 9

answer = two_sum(nums, target)


print("Result:", answer)

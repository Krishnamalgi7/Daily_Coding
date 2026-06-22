"""
Concept:
The Two Sum problem finds two numbers in an array whose sum equals a target value.

Example:
nums = [5, 9, 1, 2, 4, 15, 6, 3]
target = 13

9 + 4 = 13

Indices = [1, 4]

Program: Two Sum Problem
Description:
    Method 1: Brute Force using nested loops.
    Method 2: Using Hash Map (Dictionary).
Complexity:
    Method 1: Time O(n²) | Space O(1)
    Method 2: Time O(n) | Space O(n)
"""
from typing import List

# Method 1: Brute Force
def two_sum(nums: List[int], target: int):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):

            if nums[i] + nums[j] == target:
                return {
                    "indices": [i, j],
                    "result": f"{nums[i]} + {nums[j]} = {target}"
                }

    return None


lst = [5, 9, 1, 2, 4, 15, 6, 3]

print(two_sum(lst, 13))


# Method 2: Using Hash Map
def two_sum_hash(nums: List[int], target: int):
    n = len(nums)

    mapp = {}

    for i in range(n):

        remaining = target - nums[i]

        if remaining in mapp:
            return {
                "indices": [mapp[remaining], i],
                "result": f"{remaining} + {nums[i]} = {target}"
            }

        mapp[nums[i]] = i

    return None


lst = [5, 9, 1, 2, 4, 15, 6, 3]

print(two_sum_hash(lst, 13))


# Method 1 output :
# {'indices': [1, 4], 'result': '9 + 4 = 13'}

# Method 2 output :
# {'indices': [1, 4], 'result': '9 + 4 = 13'}


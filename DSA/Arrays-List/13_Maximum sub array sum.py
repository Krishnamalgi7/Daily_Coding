"""
Concept:
The Maximum Subarray Sum problem finds the contiguous subarray having the
largest sum.

Example:
[-2, 1, -3, 4, -1, 2, 1, -5, 4]

Maximum Subarray:
[4, -1, 2, 1]

Maximum Sum = 6

Program: Find Maximum Subarray Sum
Description:
    Method 1: Brute Force by checking all possible subarrays.
    Method 2: Kadane's Algorithm (Optimal).
Complexity:
    Method 1: Time O(n²) | Space O(1)
    Method 2: Time O(n) | Space O(1)
"""

# Method 1: Brute Force
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

n = len(nums)

maxi = float("-inf")

for i in range(n):
    total = 0

    for j in range(i, n):
        total += nums[j]
        maxi = max(maxi, total)

print(maxi)


# Method 2: Kadane's Algorithm
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

n = len(nums)

total = 0
maxi = float("-inf")

for i in range(n):

    total += nums[i]

    maxi = max(maxi, total)

    if total < 0:
        total = 0

print(maxi)


# Method 1 output : 6
# Method 2 output : 6





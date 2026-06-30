"""
Concept:
The Longest Consecutive Sequence problem finds the length of the longest sequence
of consecutive integers in an unsorted array.

Example:
[1, 99, 101, 98, 2, 5, 3, 100]

Longest Consecutive Sequence:
98, 99, 100, 101

Length = 4

Program: Find Longest Consecutive Sequence
Description:
    Method 1: Check consecutive numbers using membership testing.
    Method 2: Using a Hash Set (Optimal).
Complexity:
    Method 1: Time O(n²) | Space O(1)
    Method 2: Time O(n) | Space O(n)
"""

# Method 1: Using membership testing
nums = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]

n = len(nums)

max_count = 0

for i in range(n):

    num = nums[i]
    count = 1

    while num + 1 in nums:
        count += 1
        num += 1

    max_count = max(max_count, count)

print(max_count)


# Method 2: Using Hash Set
nums = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]

num_set = set(nums)

max_count = 0

for num in num_set:

    if num - 1 not in num_set:

        current_num = num
        count = 1

        while current_num + 1 in num_set:
            current_num += 1
            count += 1

        max_count = max(max_count, count)

print(max_count)


# Method 1 output : 4
# Method 2 output : 4


"""
Concept:
The maximum consecutive 1's problem finds the longest sequence of continuous 1's.
We count consecutive 1's using a counter. When a 0 is encountered, the count is reset.
The maximum count seen during traversal is the answer.

Example:
[1,1,0,1,1,1]

Consecutive groups:
1,1 → count = 2
1,1,1 → count = 3

Maximum = 3

Program: Find Maximum Consecutive 1's
Description:
    Using counter and tracking maximum count.

Complexity:
   Time O(n) | Space O(1)
"""

# Using counter
nums = [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]

i = 0
count = 0
max_count = 0

while i < len(nums):

    if nums[i] == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0

    i += 1

print(max_count)
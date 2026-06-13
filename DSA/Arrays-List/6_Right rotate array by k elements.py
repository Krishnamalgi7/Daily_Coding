"""
Concept:
Rotating an array by K positions to the right means moving the last K elements
to the front while shifting the remaining elements to the right.
In the iterative approach, we perform one-position right rotation K times.

Example:
[5, -2, 3, 9, 0, 6, 10, 7], k = 3

After 1 rotation:
[7, 5, -2, 3, 9, 0, 6, 10]

After 2 rotations:
[10, 7, 5, -2, 3, 9, 0, 6]

After 3 rotations:
[6, 10, 7, 5, -2, 3, 9, 0]

Program: Rotate Array by K Positions to the Right
Description:
    Method 1: Rotate one position K times using shifting.
    Method 2: Using list slicing.
Complexity:
    Method 1: Time O(n × k) | Space O(1)
    Method 2: Time O(n) | Space O(n)
"""

# Method 1: Rotate one position K times
nums = [5, -2, 3, 9, 0, 6, 10, 7]

n = len(nums)
k = 3

for _ in range(1, k + 1):
    temp = nums[n - 1]

    for i in range(n - 2, -1, -1):
        nums[i + 1] = nums[i]

    nums[0] = temp

print(nums)


# Method 2: Using slicing
nums = [5, -2, 3, 9, 0, 6, 10, 7]
#       -8 -7 -6 -5 -4 -3  -2 -1

k = 3

k = k % len(nums)

nums = nums[-k:] + nums[:-k]
#      -3 to end + start to -3
print(nums)


# Method 1 output :
# [6, 10, 7, 5, -2, 3, 9, 0]

# Method 2 output :
# [6, 10, 7, 5, -2, 3, 9, 0]


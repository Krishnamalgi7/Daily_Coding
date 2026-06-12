"""
Concept:
Rotating an array by one position to the right means moving the last element
to the first position and shifting all other elements one position to the right.

Example:
[5, -2, 3, 9, 0, 6, 10, 7]

Last element = 7

Result:
[7, 5, -2, 3, 9, 0, 6, 10]

Program: Rotate Array by One Position to the Right
Description:
    Method 1: Using list slicing.
    Method 2: Using element shifting (in-place).
Complexity:
    Method 1: Time O(n) | Space O(n)
    Method 2: Time O(n) | Space O(1)
"""

# Method 1: Using list slicing
nums = [5, -2, 3, 9, 0, 6, 10, 7]

nums = [nums[-1]] + nums[0:len(nums)-1]

print(nums)


# Method 2: Using element shifting (in-place)
nums = [5, -2, 3, 9, 0, 6, 10, 7]

n = len(nums)

temp = nums[n - 1]

for i in range(n - 2, -1, -1):
    nums[i + 1] = nums[i]

nums[0] = temp

print(nums)


# Method 1 output :
# [7, 5, -2, 3, 9, 0, 6, 10]

# Method 2 output :
# [7, 5, -2, 3, 9, 0, 6, 10]

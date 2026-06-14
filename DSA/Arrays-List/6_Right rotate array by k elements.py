"""
Concept:
Rotating an array by K positions to the right means moving the last K elements
to the front while shifting the remaining elements to the right.

Example:
[5, -2, 3, 9, 0, 6, 10, 7], k = 3

After rotation:
[6, 10, 7, 5, -2, 3, 9, 0]

Program: Rotate Array by K Positions to the Right
Description:
    Method 1: Rotate one position K times using shifting.
    Method 2: Using list slicing.
    Method 3: Using reversal algorithm (optimal).
Complexity:
    Method 1: Time O(n × k) | Space O(1)
    Method 2: Time O(n) | Space O(n)
    Method 3: Time O(n) | Space O(1)
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

k = 3
k = k % len(nums)

nums = nums[-k:] + nums[:-k]

print(nums)


# Method 3: Using reversal algorithm
#       0  1   2  3  4  5  6  7
nums = [5, -2, 3, 9, 0, 6, 10, 7]
k = 5
n = len(nums)

k = k % n

def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


reverse(nums, n - k, n - 1) #[      7,10,6,0,9]

reverse(nums, 0, n - k - 1) #[3,-2,5          ]

reverse(nums, 0, n - 1)     #[9,0,6,10,7,5,-2,3]

print(nums)


# Method 1 output :
# [6, 10, 7, 5, -2, 3, 9, 0]

# Method 2 output :
# [6, 10, 7, 5, -2, 3, 9, 0]

# Method 3 output :
# [9, 0, 6, 10, 7, 5, -2, 3]


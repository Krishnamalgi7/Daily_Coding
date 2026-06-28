"""
Concept:
Rearrange the array so that positive and negative numbers appear alternately,
starting with a positive number.

Example:
[5, 10, -3, -1, -10, 6]

Output:
[5, -3, 10, -1, 6, -10]

Program: Rearrange Array Elements by Sign
Description:
    Method 1: Store positive and negative numbers separately, then merge alternately.
    Method 2: Place positive and negative numbers directly into a result array.
Complexity:
    Method 1: Time O(n) | Space O(n)
    Method 2: Time O(n) | Space O(n)
"""

# Method 1: Using two separate lists
nums = [5, 10, -3, -1, -10, 6]

n = len(nums)

posi = []
nege = []

for i in range(n):
    if nums[i] > 0:
        posi.append(nums[i])
    else:
        nege.append(nums[i])

for i in range(len(posi)):
    nums[2 * i] = posi[i]
    nums[2 * i + 1] = nege[i]

print(nums)


# Method 2: Using result array
nums = [5, 10, -3, -1, -10, 6]

n = len(nums)

res = [0] * n

pos = 0
neg = 1

for i in range(n):

    if nums[i] >= 0:
        res[pos] = nums[i]
        pos += 2

    else:
        res[neg] = nums[i]
        neg += 2

print(res)


# Method 1 output :
# [5, -3, 10, -1, 6, -10]

# Method 2 output :
# [5, -3, 10, -1, 6, -10]


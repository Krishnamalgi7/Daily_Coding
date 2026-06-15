"""
Concept:
Moving all zeros to the end means keeping the relative order of non-zero elements
unchanged while placing all zeros at the end of the array.

Example:
[1, 2, 0, 4, 3, 0, 0, 3, 5, 1]

→ [1, 2, 4, 3, 3, 5, 1, 0, 0, 0]

Program: Move All Zeros to End
Description:
    Method 1: Using temporary array to store non-zero elements.
    Method 2: Using two-pointer swapping approach.
Complexity:
    Method 1: Time O(n) | Space O(n)
    Method 2: Time O(n) | Space O(1)
"""

# Method 1: Using temporary array
nums = [1, 2, 0, 4, 3, 0, 0, 3, 5, 1]

n = len(nums)

temp = []

for i in range(n):
    if nums[i] != 0:
        temp.append(nums[i])

n2 = len(temp)

for i in range(n2):
    nums[i] = temp[i]

for i in range(n2, n):
    nums[i] = 0

print(nums)


# Method 2: Using two pointers
nums = [1, 2, 0, 4, 3, 0, 0, 3, 5, 1]

i = 0

while i < len(nums):
    if nums[i] == 0:
        break
    i += 1

if i == len(nums):
    print("No zero elements")
else:
    j = i + 1

    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1

    print(nums)


# Method 1 output :
# [1, 2, 4, 3, 3, 5, 1, 0, 0, 0]

# Method 2 output :
# [1, 2, 4, 3, 3, 5, 1, 0, 0, 0]



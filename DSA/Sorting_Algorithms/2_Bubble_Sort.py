# It works on adjacent swaps
"""
Concept:
Bubble Sort repeatedly compares adjacent elements and swaps them if they are
in the wrong order. After each pass, the largest unsorted element "bubbles up"
to its correct position at the end of the array.

Example:
[5, 3, 8, 1]
→ Compare 5 & 3 → swap
→ Compare 5 & 8 → no swap
→ Compare 8 & 1 → swap
→ Continue until sorted

Program: Bubble Sort
Description:
    Method 1: Bubble Sort in ascending order.
    Method 2: Bubble Sort in descending order.
Complexity:
    Method 1: Time O(n²) | Space O(1)
    Method 2: Time O(n²) | Space O(1)
"""

# Method 1: Bubble Sort
nums = [5, 7, 8, 4, 1, 6, 9, 2]

n = len(nums)

for i in range(n-2, -1, -1):
    for j in range(0, i + 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)


# Method 2: Bubble Sort (Descending Order)
nums = [5, 7, 8, 4, 1, 6, 9, 2]

n = len(nums)

for i in range(n-2,-1,-1):
    for j in range(0, i + 1):
        if nums[j] < nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)

# Method 1 output : [1, 2, 4, 5, 6, 7, 8, 9]
# Method 2 output : [9, 8, 7, 6, 5, 4, 2, 1]


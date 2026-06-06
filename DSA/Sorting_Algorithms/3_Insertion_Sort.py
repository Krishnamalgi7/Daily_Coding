"""
Concept:
Insertion Sort builds a sorted portion of the array one element at a time.
We take one element (key) and insert it into its correct position among the
already sorted elements on the left.

Program: Insertion Sort
Description:
    Method 1: Insertion Sort in ascending order.
    Method 2: Insertion Sort in descending order.
Complexity:
    Method 1: Time O(n²) | Space O(1)
    Method 2: Time O(n²) | Space O(1)
"""

# Method 1: Insertion Sort (Ascending Order)
nums = [3, 5, 6, 4, 8, 9, 10, 7]
n = len(nums)

for i in range(1, n):
    key = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1

    nums[j + 1] = key

print(nums)


# Method 2: Insertion Sort (Descending Order)
nums = [3, 5, 6, 4, 8, 9, 10, 7]
n = len(nums)

for i in range(1, n):
    key = nums[i]
    j = i - 1

    while j >= 0 and nums[j] < key:
        nums[j + 1] = nums[j]
        j -= 1

    nums[j + 1] = key

print(nums)


# Method 1 output :
# [3, 4, 5, 6, 7, 8, 9, 10]

# Method 2 output :
# [10, 9, 8, 7, 6, 5, 4, 3]


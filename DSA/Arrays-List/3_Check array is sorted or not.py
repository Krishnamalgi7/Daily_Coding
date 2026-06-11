"""
Concept:
A sorted array is one where every element is smaller than or equal to the next element.
We compare adjacent elements:
nums[i] and nums[i+1].
If any element is greater than the next one, the array is not sorted.

Example:
[3, 5, 6, 8, 9]
→ 3 < 5 < 6 < 8 < 9
→ Sorted

[3, 5, 8, 6]
→ 8 > 6
→ Not Sorted

Program: Check if an Array is Sorted
Description:
    Method 1: Compare adjacent elements using a loop.
    Method 2: Compare array with its sorted version.
Complexity:
    Method 1: Time O(n) | Space O(1)
    Method 2: Time O(n log n) | Space O(n)
"""

# Method 1: Using adjacent element comparison
def check_sorted(nums):
    n = len(nums)

    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return False

    return True

nums = [3, 5, 6, 8, 9, 10, 20]
print(check_sorted(nums))


# Method 2: Using sorted()
nums = [3, 5, 8, 6]

print(nums == sorted(nums))


# Method 1 output : True
# Method 2 output : False


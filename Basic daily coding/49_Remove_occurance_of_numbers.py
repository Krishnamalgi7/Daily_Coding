"""
Concept:
Removing all occurrences of an element means deleting every appearance of a target value
from the list. We repeatedly check if the target exists and remove it until no occurrences remain.

Example:
[1, 1, 2, 3, 1, 4], target = 1
→ [2, 3, 4]

Program: Remove All Occurrences of an Element
Description:
    Method 1: Using remove() repeatedly until target is not found.
    Method 2: Using list comprehension.
Complexity:
    Method 1: Time O(n²) | Space O(1)
    Method 2: Time O(n) | Space O(n)
"""

# Method 1: Using remove() repeatedly
def removge_occurances(lst, target):
    while target in lst:
        lst.remove(target)
    return lst

nums = [1,1,1,1,2,2,3,4,5,6,6,6,6,6,6,6]

print(removge_occurances(nums, 1))


# Method 2: Using list comprehension (intentional different input)
nums = [2, 3, 2, 4, 2, 5, 6]

target = 2

result = [num for num in nums if num != target]

print(result)


# Method 1 output :
# [2, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 6]

# Method 2 output :
# [3, 4, 5, 6]

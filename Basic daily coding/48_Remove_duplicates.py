"""
Concept:
Removing duplicates means keeping only the first occurrence of each element.
We check whether an element already exists in the result list.
If it does not exist, we add it; otherwise, we skip it.

Example:
[1, 1, 2, 3, 2, 4]
→ [1, 2, 3, 4]

Program: Remove Duplicates from a Arrays-List
Description:
    Method 1: Using loop and membership check.
    Method 2: Using set() while preserving order with dict.fromkeys().
Complexity:
    Method 1: Time O(n²) | Space O(n)
    Method 2: Time O(n) | Space O(n)
"""

# Method 1: Using loop and membership check
def remove_duplicates(lst):
    result = []

    for num in lst:
        if num not in result:
            result.append(num)

    return result

num = [1,1,2,3,4,5,5,5,5,6,5,5,8,10,13,23,23,23,23,23,23,23,23,3]

print(remove_duplicates(num))


# Method 2: Using dict.fromkeys()
num = [1, 1, 2, 2, 3, 4, 4, 5]

result = list(dict.fromkeys(num))

print(result)


# Method 1 output :
# [1, 2, 3, 4, 5, 6, 8, 10, 13, 23]

# Method 2 output :
# [1, 2, 3, 4, 5]

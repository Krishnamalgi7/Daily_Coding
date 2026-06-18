"""
Concept:
Linear Search checks each element one by one from left to right until the target
element is found. If found, return its index; otherwise return -1.

Example:
[5, 9, 3, 4, 5]
Target = 4

→ Check 5 ❌
→ Check 9 ❌
→ Check 3 ❌
→ Check 4 ✅

Index = 3

Program: Linear Search
Description:
    Method 1: Using loop and index comparison.
    Method 2: Using built-in index() method.
Complexity:
    Method 1: Time O(n) | Space O(1)
    Method 2: Time O(n) | Space O(1)
"""

# Method 1: Linear Search
def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1
#       0  1  2  3  4  5  6  7   8   9
nums = [5, 9, 3, 4, 5, 6, 8, 10, -4, -5]

target = 4

print(linear_search(nums, target))


# Method 2: Using built-in index()
nums = [10, 20, 30, 40, 50]

target = 40

if target in nums:
    print(nums.index(target))
else:
    print(-1)


# Method 1 output : 3
# Method 2 output : 3



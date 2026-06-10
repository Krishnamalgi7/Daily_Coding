"""
Concept:
The Second Largest element is the largest element after the first largest element.
We can either:
1. Find the largest element first, then find the largest among the remaining elements.
2. Track both largest and second largest in a single traversal.

Example:
[55, 32, 97, -55, 45, 32, 88, 21]
→ Largest = 97
→ Second Largest = 88

Program: Find Second Largest Element in an Array
Description:
    Method 1: Find largest first, then find second largest.
    Method 2: Find largest and second largest in a single traversal.
Complexity:
    Method 1: Time O(n) | Space O(1)
    Method 2: Time O(n) | Space O(1)
"""

# Method 1: Two Traversals
nums = [55, 32, 97, -55, 45, 32, 88, 21]
n = len(nums)

largest = float("-inf")
sec_largest = float("-inf")

for i in range(n):
    if nums[i] > largest:
        largest = nums[i]

for i in range(n):
    if nums[i] > sec_largest and nums[i] != largest:
        sec_largest = nums[i]

if sec_largest == float("-inf"):
    print("No second largest element exists")
else:
    print(f"Second Largest = {sec_largest}")


# Method 2: Single Traversal
def second_largest(nums):
    largest = float("-inf")
    sec_largest = float("-inf")

    for num in nums:
        if num > largest:
            sec_largest = largest
            largest = num

        elif num > sec_largest and num != largest:
            sec_largest = num

    if sec_largest == float("-inf"):
        return "No second largest element exists"

    return f"Second Largest = {sec_largest}"


print(second_largest([55, 32, 97, -55, 45, 32, 88, 21]))

# Method 1 output :
# Second Largest = 88

# Method 2 output :
# Second Largest = 88

# Edge Case:
# Input : [5, 5, 5]
# Output : No second largest element exists


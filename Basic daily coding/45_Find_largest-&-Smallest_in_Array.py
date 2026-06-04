"""
Concept:
To find the maximum or minimum element in an array, we compare each element
with the current maximum/minimum value and update it when a larger/smaller
element is found.

Example:
[5, 2, 9, 1]
→ Maximum = 9
→ Minimum = 1

Program: Find Maximum and Minimum Element in an Array
Description:
    Method 1: Iterative approach using comparison.
    Method 2: Using built-in max() and min() functions.
Complexity:
    Method 1: Time O(n) | Space O(1)
    Method 2: Time O(n) | Space O(1)
"""

# Method 1: Iterative Approach
nums = [5,5,8,7,-8,9,5,4,-10,55,33,100,122,-154,85,225,638,369,341,800,145,1]

maxi = float('-inf')

for num in nums:
    if num > maxi:
        maxi = num

print(f"Maximum is: {maxi}")

# Find minimum in array
nums = [5,5,8,7,-8,9,5,4,-10,55,33,100,122,-154,85,225,638,369,341,800,145,1]

mini = float('inf')

for num in nums:
    if num < mini:
        mini = num

print(f"Minimum is: {mini}")


# Method 2: Using built-in functions (intentional different input)
nums = [10, -5, 25, 100, 3]

print(f"Maximum is: {max(nums)}")
print(f"Minimum is: {min(nums)}")


# Method 1 output :
# Maximum is: 800
# Minimum is: -154

# Method 2 output :
# Maximum is: 100
# Minimum is: -5



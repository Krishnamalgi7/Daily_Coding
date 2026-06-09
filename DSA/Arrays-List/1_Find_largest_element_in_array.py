"""
Concept:
To find the maximum element in an array, we compare each element with the current
maximum value and update it whenever a larger element is found.

Example:
[5, 2, 9, 1]
→ Maximum = 9

Program: Find Maximum Element in an Array
Description:
    Method 1: Using a variable initialized to negative infinity.
    Method 2: Using the first element as the initial maximum.
    Method 3: Using max() on two values during iteration.
    Method 4: Using built-in max() function.
Complexity:
    Method 1: Time O(n) | Space O(1)
    Method 2: Time O(n) | Space O(1)
    Method 3: Time O(n) | Space O(1)
    Method 4: Time O(n) | Space O(1)
"""

# Method 1: Using negative infinity
nums = [55, 32, -97, 99, 3, 67, 150]

maxi = float('-inf')

for i in nums:
    if i > maxi:
        maxi = i

print(f"Maximum is: {maxi}")


# Method 2: Using first element
nums = [2, 3, 4, 5, 6, 7, 8, 9, 90, -800, 350, -2000]
n = len(nums)

largest = nums[0]

for i in range(0, n):
    if nums[i] > largest:
        largest = nums[i]

print(f"Maximum is: {largest}")


# Method 3: Using max() during iteration
nums = [4, -85, 96, -4, -1, 8]
n = len(nums)

largest = nums[0]

for i in range(0, n):
    largest = max(nums[i], largest)

print(f"Maximum is: {largest}")


# Method 4: Using built-in max()
nums = [10, 25, -5, 100, 45]

print(f"Maximum is: {max(nums)}")


# Method 1 output : Maximum is: 150
# Method 2 output : Maximum is: 350
# Method 3 output : Maximum is: 96
# Method 4 output : Maximum is: 100



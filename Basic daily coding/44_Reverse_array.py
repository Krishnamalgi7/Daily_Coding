"""
Concept:
Array reversal means swapping elements from both ends towards the center.
In recursion, we swap arr[left] and arr[right], then move inwards:
left + 1 and right - 1.
The process stops when left >= right.

Example:
[1, 2, 3, 4]
→ swap 1 & 4
→ swap 2 & 3
→ [4, 3, 2, 1]

Program: Reverse an Array Using Recursion
Description:
    Method 1: Recursive approach using two pointers.
    Method 2: Using built-in reverse slicing.
Complexity:
    Method 1: Time O(n) | Space O(n)
    Method 2: Time O(n) | Space O(n)
"""

# Method 1: Recursive Approach
arr = [2, 4, 5, 7, 9, 3, 1]

def reverse(arr, left, right):
    if left >= right:
        return arr

    arr[left], arr[right] = arr[right], arr[left]

    return reverse(arr, left + 1, right - 1)

print(reverse(arr, 0, len(arr) - 1))


# Method 2: Using slicing
arr = [10, 20, 30, 40, 50]

print(arr[::-1])


# Method 1 output : [1, 3, 9, 7, 5, 4, 2]
# Method 2 output : [50, 40, 30, 20, 10]


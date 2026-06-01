"""
Concept:
Selection Sort works by repeatedly finding the smallest element from the unsorted part
of the array and placing it at its correct position.
For each index i, we find the minimum element from i to n-1 and swap it with nums[i].

Example:
[5, 3, 4, 1]
→ Find min (1) and place at index 0, this keeps on repeating until the array is sorted
→ [1, 3, 4, 5]

Program: Selection Sort
Description:
    Method 1: Manual Selection Sort using nested loops.
    Method 2: Sort in descending order
    Method 3: Using built-in sorted() function.
Complexity:
    Method 1: Time O(n²) | Space O(1)
    Method 2: Time O(n²) | Space O(1)
    Method 2: Time O(n log n) | Space O(n)
"""

# Method 1: Selection Sort
nums = [5, 7, 8, 4, 1, 6, 9, 2]

def selection_sort(nums):
    n = len(nums)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums

print(selection_sort(nums))

# Method 2: Selection Sort in Descending order
def selection_sort_rev(nums):
    n = len(nums)

    for i in range(n):
        max_idx = i

        for j in range(i + 1, n):
            if nums[j] > nums[max_idx]:
                max_idx = j

        nums[i], nums[max_idx] = nums[max_idx], nums[i]

    return nums

print(selection_sort_rev(nums))

# Method 3: Using built-in sorted()
nums = [9, 4, 7, 1, 3]

print(sorted(nums))


# Method 1 output : [1, 2, 4, 5, 6, 7, 8, 9]
# Method 2 o/p = [9, 8, 7, 6, 5, 4, 2, 1]
# Method 2 output : [1, 3, 4, 7, 9]


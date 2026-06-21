"""
Concept:
Given an array containing numbers from 0 to n with one or more missing values,
find the missing number(s).

Example:
[0,1,2,3,4,5,6,7,8,10]

Missing Number = 9

Program: Find Missing Number(s) in an Array
Description:
    Method 1: Using membership testing to find a single missing number.
    Method 2: Using membership testing to find first two missing numbers.
    Method 3: Using frequency map.
    Method 4: Using sum formula.
Complexity:
    Method 1: Time O(n²) | Space O(1)
    Method 2: Time O(n²) | Space O(1)
    Method 3: Time O(n) | Space O(n)
    Method 4: Time O(n) | Space O(1)
"""

# Method 1: Using membership testing (single missing number)
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
n = len(nums)

def find_missing(nums):
    for i in range(n + 1):
        if i not in nums:
            return i

print(find_missing(nums))


# Method 2: Find first two missing numbers
nums = [0, 1, 2, 3, 4, 7, 8, 9, 10]

def find_second_missing(nums):
    missing = []

    for i in range(0, 11):
        if i not in nums:
            missing.append(i)

    return missing[:2]

print(find_second_missing(nums))


# Method 3: Using frequency map
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

n = len(nums)

def find_missing_number(nums):
    freq = {}

    for i in range(n + 1):
        freq[i] = 0

    for num in nums:
        freq[num] = 1

    for k, v in freq.items():
        if v == 0:
            return k

print(find_missing_number(nums))


# Method 4: Using sum formula
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

def find_missing_number_fast(nums):
    n = len(nums)

    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum

print(find_missing_number_fast(nums))


# Method 1 output : 9
# Method 2 output : [5, 6]
# Method 3 output : 8
# Method 4 output : 8


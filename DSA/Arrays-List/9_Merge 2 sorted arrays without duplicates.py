"""
Concept:
The Union of two sorted arrays contains all unique elements present in either array.
Using two pointers, we compare elements from both arrays and add the smaller one
to the result. Duplicate elements are skipped.

Example:
nums1 = [1, 1, 4, 6]
nums2 = [1, 2, 6, 7]

Union:
[1, 2, 4, 6, 7]

Program: Union of Two Sorted Arrays
Description:
    Method 1: Using two pointers on sorted arrays.
    Method 2: Using set union.
Complexity:
    Method 1: Time O(n + m) | Space O(n + m)
    Method 2: Time O(n + m) | Space O(n + m)
"""

# Method 1: Two Pointer Approach
nums1 = [1, 1, 1, 4, 6, 7]
nums2 = [1, 2, 3, 6, 7, 8, 9, 10]

n = len(nums1)
m = len(nums2)

result = []

i = 0
j = 0

while i < n and j < m:

    if nums1[i] <= nums2[j]:

        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])

        i += 1

    else:

        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])

        j += 1


while i < n:

    if len(result) == 0 or result[-1] != nums1[i]:
        result.append(nums1[i])

    i += 1


while j < m:

    if len(result) == 0 or result[-1] != nums2[j]:
        result.append(nums2[j])

    j += 1


print(result)


# Method 2: Using set union
nums1 = [1, 1, 1, 4, 6, 7]
nums2 = [1, 2, 3, 6, 7, 8, 9, 10]

result = sorted(set(nums1).union(set(nums2)))

print(result)


# Method 1 output :
# [1, 2, 3, 4, 6, 7, 8, 9, 10]

# Method 2 output :
# [1, 2, 3, 4, 6, 7, 8, 9, 10]


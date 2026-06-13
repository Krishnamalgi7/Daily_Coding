"""
Concept:
Removing duplicates from a sorted array means keeping only one occurrence of each element.
We use a dictionary to store unique elements as keys because dictionary keys are unique.
Then we overwrite the original array with those unique values.

Example:
[1,1,2,3,3,4]
→ [1,2,3,4]

Program: Remove Duplicates from a Sorted Array
Description:
    Method 1: Using dictionary to store unique elements.
    Method 2: Using two-pointer technique (optimized).
Complexity:
    Method 1: Time O(n) | Space O(n)
    Method 2: Time O(n) | Space O(1)
"""

# Method 1: Using dictionary
nums = [1,1,2,3,3,4,4,5,5,6,7,8,9,10,11,11]

n = len(nums)

freq_map = {}

for i in range(n):
    freq_map[nums[i]] = 0

j = 0

for k in freq_map:
    nums[j] = k
    j += 1
    print(k, end=" ")

print()


# Method 2: Using two pointers
nums = [1,1,2,3,3,4,4,5,5,6,7,8,9,10,11,11,11]

n = len(nums)

if n==0:
    print("Empty List")
else:
    i=0

    for j in range(1,n):
        if nums[i] != nums[j]:
            i=i+1
            nums[i] = nums[j]

    print(*nums[:i+1]) # * This unpacks the list and prints each element separated by a space

# Method 1 output :
# 1 2 3 4 5 6 7 8 9 10 11

# Method 2 output :
# 1 2 3 4 5 6 7 8 9 10 11

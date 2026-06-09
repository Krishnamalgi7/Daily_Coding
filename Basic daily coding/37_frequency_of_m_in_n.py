"""
Concept:
Frequency means counting how many times each element appears in a list.
We first store frequencies of elements in a dictionary.
Then for another list, we check if elements exist in the dictionary and print counts.

Example:
n = [1,2,2,3], m = [2,3,4]
→ 2 occurs 2 times
→ 3 occurs 1 time
→ 4 occurs 0 times

Program: Frequency of Elements from One Arrays-List in Another
Description:
    Method 1: Using dictionary to store frequency (your logic).
    Method 2: Using collections.Counter (built-in optimized).
Complexity:
    Method 1: Time O(n + m) | Space O(n)
    Method 2: Time O(n + m) | Space O(n)
"""

# Method 1: Using dictionary
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

freq = {}

for num in n:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for num in m:
    if num in freq:
        print(num, 'occurs', freq[num], 'times')
    else:
        print(num, 'occurs 0 times')

print()

# Method 2: Using Counter
from collections import Counter

n = [1, 2, 2, 3, 3, 3]
m = [2, 3, 4]

freq = Counter(n)

for num in m:
    print(num, 'occurs', freq.get(num, 0), 'times')


# Method 1 output :
# 10 occurs 1 times
# 111 occurs 0 times
# 1 occurs 1 times
# 9 occurs 0 times
# 5 occurs 4 times
# 67 occurs 0 times
# 2 occurs 2 times

# Method 2 output :
# 2 occurs 2 times
# 3 occurs 3 times
# 4 occurs 0 times


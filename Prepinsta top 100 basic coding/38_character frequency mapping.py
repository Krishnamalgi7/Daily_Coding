"""
Concept:
Frequency means counting how many times each character appears.
We first store frequency of characters from one string.
Then for another string, we check each character and print its count.

Example:
s1 = "aabbc", s2 = "abcx"
→ a occurs 2 times
→ b occurs 2 times
→ c occurs 1 time
→ x occurs 0 times

Program: Frequency of Characters from One String in Another
Description:
    Method 1: Using dictionary to store frequency (your logic style).
    Method 2: Using collections.Counter (built-in optimized).
Complexity:
    Method 1: Time O(n + m) | Space O(n)
    Method 2: Time O(n + m) | Space O(n)
"""

# Method 1: Using dictionary
s1 = "aabbccdde"
s2 = "abcxyz"

freq = {}

for ch in s1:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in s2:
    if ch in freq:
        print(ch, 'occurs', freq[ch], 'times')
    else:
        print(ch, 'occurs 0 times')

print()
# Method 2: Using Counter
from collections import Counter

s1 = "mississippi"
s2 = "sipz"

freq = Counter(s1)

for ch in s2:
    print(ch, 'occurs', freq.get(ch, 0), 'times')

# Method 1 output :
# a occurs 2 times
# b occurs 2 times
# c occurs 2 times
# x occurs 0 times
# y occurs 0 times
# z occurs 0 times

# Method 2 output :
# s occurs 4 times
# i occurs 4 times
# p occurs 2 times
# z occurs 0 times

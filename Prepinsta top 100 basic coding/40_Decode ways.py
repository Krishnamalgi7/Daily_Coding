"""
Concept:
A digit string can be decoded where:
1 -> A, 2 -> B, ..., 26 -> Z
We count how many ways the string can be split into valid 1-digit or 2-digit numbers (1–26).
We use Dynamic Programming from right to left to store number of ways.

Example:
"12" → (1,2) = AB, (12) = L → Total = 2 ways

Program: Count Possible Decodings of a Digit Sequence
Description:
    Method 1: Recursive approach checking single and double digit choices.
    Method 2: Optimized Dynamic Programming (bottom-up using hashmap).
Complexity:
    Method 1: Time O(2^n) | Space O(n)
    Method 2: Time O(n) | Space O(n)
"""

# Method 1: Recursive Approach
def count_decodings(s, i):
    if i == len(s):
        return 1
    if s[i] == '0':
        return 0

    count = count_decodings(s, i + 1)

    if i + 1 < len(s) and int(s[i:i+2]) <= 26:
        count += count_decodings(s, i + 2)

    return count

s = "12"
print(f"Total decodings are {count_decodings(s, 0)}")


# Method 2: DP
def numDecodings(s: str) -> int:
    dp = {len(s): 1}

    for i in range(len(s) - 1, -1, -1):
        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]

        if (i + 1 < len(s) and 
            (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456"))):
            dp[i] += dp[i + 2]

    return dp[0]

s = "226"
print(f"Total decodings are {numDecodings(s)}")


# Method 1 output : Total decodings are 2
# Method 2 output : Total decodings are 3

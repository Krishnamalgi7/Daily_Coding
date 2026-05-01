"""
Concept:
The maximum number of handshakes among n people occurs when each person
shakes hands with every other person exactly once.
Formula:
Handshakes = n(n - 1) / 2

Example:
n = 5 → 5×4/2 = 10 handshakes

Program: Find Maximum Number of Handshakes
Description:
    Method 1: Using nested loops to count all unique pairs.
    Method 2: Using direct formula n(n-1)/2.
Complexity:
    Method 1: Time O(n^2) | Space O(1)
    Method 2: Time O(1) | Space O(1)
"""

# Method 1: Using nested loops
n = 5
count = 0

for i in range(n):
    for j in range(i+1, n):
        count = count + 1

print(f"Maximum number of handshakes is {count}")


# Method 2: Using formula
n = 6

handshakes = n * (n - 1) // 2

print(f"Maximum number of handshakes is {handshakes}")


# Method 1 output : Maximum number of handshakes is 10
# Method 2 output : Maximum number of handshakes is 15

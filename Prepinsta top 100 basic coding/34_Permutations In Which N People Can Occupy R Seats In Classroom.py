"""
Concept:
Permutation means arranging r items from n distinct items where order matters.
Formula:
nPr = n! / (n - r)!

Example:
n = 5, r = 2 → 5P2 = 5! / 3! = 20

Program: Calculate Permutations (nPr)
Description:
    Method 1: Using factorial calculation manually.
    Method 2: Using built-in math.perm().
Complexity:
    Method 1: Time O(n) | Space O(1)
    Method 2: Time O(r) | Space O(1)
"""

# Method 1: Using factorial
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

n = 5
r = 2

if r > n or n < 0 or r < 0:
    print("Invalid input")
else:
    result = factorial(n) // factorial(n - r)
    print(f"Permutation is {result}")


# Method 2: Using built-in math.perm()
import math

n = 6
r = 3

if r > n or n < 0 or r < 0:
    print("Invalid input")
else:
    result = math.perm(n, r)
    print(f"Permutation is {result}")


# Method 1 output : Permutation is 20
# Method 2 output : Permutation is 120


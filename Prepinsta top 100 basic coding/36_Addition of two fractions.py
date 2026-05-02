"""
Concept:
To add two fractions:
(a/b) + (c/d) = (a*d + b*c) / (b*d)
Then simplify the result by dividing numerator and denominator by their GCD.

Example:
1/2 + 3/4 → (1×4 + 2×3) / (2×4) = (4 + 6)/8 = 10/8 = 5/4

Program: Add Two Fractions
Description:
    Method 1: Using manual formula and simplifying with GCD.
    Method 2: Using built-in fractions.Fraction class.
Complexity:
    Method 1: Time O(log n) | Space O(1)
    Method 2: Time O(log n) | Space O(1)
"""

# Method 1: Manual calculation
num1, den1 = 1, 2
num2, den2 = 3, 4

num = num1 * den2 + num2 * den1
den = den1 * den2

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

g = gcd(num, den)

num //= g
den //= g

print(f"Sum of fractions is {num}/{den}")


# Method 2: Using fractions module
from fractions import Fraction

f1 = Fraction(2, 3)
f2 = Fraction(3, 5)

result = f1 + f2

print(f"Sum of fractions is {result}")


# Method 1 output : Sum of fractions is 5/4
# Method 2 output : Sum of fractions is 19/15

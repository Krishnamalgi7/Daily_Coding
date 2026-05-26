"""
Concept:
A Perfect Square is a number that can be written as the product of an integer with itself.
We find the square root using (num ** 0.5), convert it to integer, and check:
(root * root == num). If true, it is a perfect square.

Example:
16 → sqrt = 4 → 4 × 4 = 16 → Perfect Square

Program: Check if a Number is Perfect Square
Description:
    Method 1: Using square root and verifying by multiplication.
    Method 2: Using math.isqrt() for precise integer square root.
Complexity:
    Method 1: Time O(1) | Space O(1)
    Method 2: Time O(1) | Space O(1)
"""

# Method 1: Using square root
def is_perfect_square(num):
    if num < 0:
        return False

    root = int(num ** 0.5)
    return root * root == num

number = 16

if is_perfect_square(number):
    print(f"{number} is a Perfect Square")
else:
    print(f"{number} is not a perfect square")


# Method 2: Using math.isqrt() (intentional different input)
import math

num = 20

root = math.isqrt(num)

if root * root == num:
    print(f"{num} is a Perfect Square")
else:
    print(f"{num} is not a perfect square")


# Method 1 output : 16 is a Perfect Square
# Method 2 output : 20 is not a perfect square

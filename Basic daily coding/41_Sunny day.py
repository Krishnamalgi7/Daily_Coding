"""
Concept:
A number is said to be a Sunny Number if the next number is a perfect square.
That means:
(num + 1) should be a perfect square.

Example:
8 → 8 + 1 = 9 → 9 is a perfect square → Sunny Number

Program: Check if a Number is Sunny Number
Description:
    Method 1: Using square root check manually.
    Method 2: Using math.isqrt() built-in function.
Complexity:
    Method 1: Time O(1) | Space O(1)
    Method 2: Time O(1) | Space O(1)
"""

# Method 1: Manual square root check
num = 8

next_num = num + 1

root = int(next_num ** 0.5)

if root * root == next_num:
    print(f"{num} is a Sunny Number")
else:
    print(f"{num} is not a Sunny Number")


# Method 2: Using math.isqrt()
import math

num = 10

next_num = num + 1

root = math.isqrt(next_num)

if root * root == next_num:
    print(f"{num} is a Sunny Number")
else:
    print(f"{num} is not a Sunny Number")


# Method 1 output : 8 is a Sunny Number
# Method 2 output : 10 is not a Sunny Number


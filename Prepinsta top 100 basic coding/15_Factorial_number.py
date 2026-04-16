"""
Concept:
Factorial of a number n is the product of all positive integers from 1 to n.
We multiply numbers sequentially using a loop (factorial = factorial * i).
For n = 5 → 5! = 5 × 4 × 3 × 2 × 1. = 120

Program: Find Factorial of a Number
Description:
    Method 1: Iterative approach using loop multiplication.
    Method 2: Using Python built-in math.factorial().
Complexity:
    Method 1: Time O(n) | Space O(1)
    Method 2: Time O(n) | Space O(1)
"""

# Method 1: Iterative Approach
def factorial(n):

    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        print(f"{n}! is ", end="")

    factorial = 1

    for i in range(1,n+1):
        factorial = factorial * i
    return factorial

num = 5

res = factorial(num)

print(res)


# Method 2: Using built-in function
import math

num = 6

res = math.factorial(num)

print(f"The Factorial of {num} is {res}")


# Method 1 output : 5! is 120
# Method 2 output : The Factorial of 6 is 720
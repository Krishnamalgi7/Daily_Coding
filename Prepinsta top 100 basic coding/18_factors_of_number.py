"""
Concept:
Factors of a number are all integers that divide the number completely (num % i == 0).
We check every number from 1 to num and collect those which divide the number without remainder.

Program: Find All Factors of a Number
Description:
    Method 1: Iterative approach checking all numbers from 1 to n.
    Method 2: Optimized approach using square root (checking pairs).
Complexity:
    Method 1: Time O(n) | Space O(n)
    Method 2: Time O(sqrt(n)) | Space O(n)
"""

# Method 1: Iterative Approach
num = 10

factors = []

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

print("Factors of", num, "are", *factors)


# Method 2: Optimized using sqrt (intentional different input)
import math

num = 36
factors = []

for i in range(1, int(math.sqrt(num)) + 1):
    if num % i == 0:
        factors.append(i)
        if i != num // i:
            factors.append(num // i)

factors.sort()

print("Factors of", num, "are", *factors)


# Method 1 output : Factors of 10 are 1 2 5 10
# Method 2 output : Factors of 36 are 1 2 3 4 6 9 12 18 36

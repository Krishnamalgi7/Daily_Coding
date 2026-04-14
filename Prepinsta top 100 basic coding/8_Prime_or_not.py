"""
Concept:
A prime number is a number greater than 1 that has only two factors: 1 and itself.
This means it cannot be divided evenly by any other number. Examples of prime
numbers include 2, 3, 5, and 7, while numbers like 4 and 6 are not prime
because they have more than two factors.

Program: Check if a Number is Prime
Description:
    Method 1: Iterative approach checking for divisors from 2 up to n-1.
    Method 2: Optimized approach using the Square Root rule.
Complexity:
    Method 1: Time O(n) | Space O(1)
    Method 2: Time O(sqrt(n)) | Space O(1)
"""
# Method 1: Iterative Approach
# We start the loop from 2 because 1 divides everything.
num = 120
flag = 0

if num < 2:
    flag = 1

for i in range(2,num):
    if num % i == 0:
        flag = 1
        break

if flag == 1:
    print(f"The number {num} is a prime number.")
else:
    print(f"The number {num} is not a prime number.")


# Method 2: Optimized approach using math.sqrt library
import math

if num >= 2:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: flag = 1; break

print(f"Method 2: {num} is {'not a prime' if flag == 1 else 'a prime'} number.")
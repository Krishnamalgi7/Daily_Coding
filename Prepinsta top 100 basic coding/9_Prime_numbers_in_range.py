"""
Concept:
Prime numbers are numbers greater than 1 that have only two factors: 1 and itself.
To find prime numbers in a range, we check each number and determine whether it
has any divisors other than 1 and itself.

Program: Find Prime Numbers in a Given Range
Description:
    Method 1: An iterative approach that checks divisibility of each number from 2 up to the square root of the number to determine if it is prime
    Note: Checking till n−1 is slower (less efficient) so we use square root approach
    Method 2: Using sympy library for prime number generation.
Complexity:
    Method 1: Time O(n^2) | Space O(n)
    Method 2: Depends on library implementation
"""

# Method 1: Iterative Approach
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

prime_list = []

for current_num in range(num1, num2 + 1):
    if current_num < 2:
        continue

    for factor in range(2, int(current_num**0.5) + 1):
        if current_num % factor == 0:
            break
    else:
        prime_list.append(current_num)

print(f"The Prime numbers are: {prime_list}")

# Method 2: Using inbuilt library (sympy)
from sympy import primerange

num1 = 1
num2 = 10

prime_list = list(primerange(num1, num2+1))

print(f"The Prime numbers are: {prime_list}")

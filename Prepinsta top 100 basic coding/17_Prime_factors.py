"""
Concept:
Prime factorization means expressing a number as a product of its prime numbers.
We repeatedly divide the number by the smallest possible divisor (starting from 2).
If a number is divisible (n % i == 0), we add it to the list and divide n by i.
This continues until n becomes 1.

Program: Find Prime Factors of a Number
Description:
    Method 1: Iterative approach checking divisibility from 2 to n.
    Method 2: Optimized approach using square root limit.
Complexity:
    Method 1: Time O(n) | Space O(log n)
    Method 2: Time O(sqrt(n)) | Space O(log n)
"""

# Method 1: Iterative Approach
num = 10
n = num

Prime_factors = []

if n == 1:
    print('1 has no prime factors')
else:
    for i in range(2, n+1):
        while n % i == 0:
            Prime_factors.append(i)
            n = n // i

    print("Prime factors of", num, "are", *Prime_factors)


# Method 2: Optimized using sqrt (intentional different input)
import math

num = 84
n = num
factors = []

# handle 2 separately
while n % 2 == 0:
    factors.append(2)
    n //= 2

# check odd numbers only
for i in range(3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
        factors.append(i)
        n //= i

# if remaining n is prime
if n > 2:
    factors.append(n)

print("Prime factors of", num, "are", *factors)


# Method 1 output : Prime factors of 10 are 2 5
# Method 2 output : Prime factors of 84 are 2 2 3 7

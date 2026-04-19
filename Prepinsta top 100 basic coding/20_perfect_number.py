"""
Concept:
A Perfect number is a number that is equal to the sum of its proper divisors
(excluding the number itself). We check divisors using (num % i == 0) and add them.
If the total sum equals the original number, it is a perfect number.

Example:
6 → Factors: 1, 2, 3 → Sum = 6 → Perfect Number

Program: Check if a Number is Perfect Number
Description:
    Method 1: Iterative approach checking all divisors from 1 to n-1.
    Method 2: Optimized approach using square root (checking divisor pairs).
Complexity:
    Method 1: Time O(n) | Space O(1)
    Method 2: Time O(sqrt(n)) | Space O(1)
"""

# Method 1: Iterative Approach
num = 6

res = 0

for i in range(1, num):
    if num % i == 0:
        res += i

if res == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

# Method 2: Optimized using sqrt
import math

def is_perfect_optimized(num):
    if num <= 1:
        return False

    total_sum = 1
    sqrt_n = int(math.sqrt(num))

    for i in range(2, sqrt_n + 1):
        if num % i == 0:
            total_sum += i
            if i * i != num:
                total_sum += num // i

    return total_sum == num

num = 6
if is_perfect_optimized(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

# Method 1 output : 6 is a perfect number
# Method 2 output : 6 is a perfect number

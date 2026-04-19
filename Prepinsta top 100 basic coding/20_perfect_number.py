"""
Concept:
A Perfect number is a number that is equal to the sum of its proper divisors (excluding the number itself).
We check divisors using (num % i == 0) and add them. If the total sum equals the original number,it is a perfect number.
Example: 6 → Factors: 1, 2, 3 → Sum = 6 → Perfect Number

Program: Check if a Number is Perfect Number
Description:
    Method 1: Iterative approach checking all divisors from 1 to n-1.
    Method 2: Optimized approach checking only up to n//2.
Complexity:
    Method 1: Time O(n) | Space O(1)
    Method 2: Time O(n/2) ≈ O(n) but faster in practice | Space O(1)
"""

# Method 1: Iterative Approach
num = 6

res = 0

for i in range(1,num):
    if num % i == 0:
        res += i

if res== num:
    print(f"The number {num} is a perfect number")
else:
    print(f"The number {num} is not a perfect number")


# Method 2: Optimized (intentional different input)
number = 10
res = 0

for i in range(1, number // 2 + 1):
    if number % i == 0:
        res += i

if res == number:
    print(f"The number {number} is a perfect number")
else:
    print(f"The number {number} is not a perfect number")


# Method 1 output : The number 6 is a perfect number
# Method 2 output : The number 10 is not a perfect number


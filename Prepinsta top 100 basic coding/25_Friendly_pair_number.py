"""
Concept:
A Friendly Pair consists of two numbers whose abundancy index is the same.
Abundancy index = (sum of proper divisors) / number.
Instead of division, we compare using cross multiplication:
(sum1 * num2 == sum2 * num1) to avoid floating-point precision errors.

Example:
6 → sum = 1+2+3 = 6 → 6/6 = 1
28 → sum = 1+2+4+7+14 = 28 → 28/28 = 1
→ Friendly Pair

Program: Check if Two Numbers are Friendly Pair
Description:
    Method 1: Compute sum of divisors separately and compare using multiplication.
    Method 2: Using optimized divisor sum (√n approach).
Complexity:
    Method 1: Time O(n1 + n2) | Space O(1)
    Method 2: Time O(√n1 + √n2) | Space O(1)
"""

# Method 1: Iterative Approach
num1, num2 = 6, 28

sum1 = 0
for i in range(1, num1):
    if num1 % i == 0:
        sum1 += i

sum2 = 0
for i in range(1, num2):
    if num2 % i == 0:
        sum2 += i

if sum1 * num2 == sum2 * num1:
    print("Yes they are friendly pair")
else:
    print("No they are not friendly pair")


# Method 2: Optimized Square Root Approach
def divisor_sum(n):
    total = 0

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i * i != n:
                total += n // i

    return total

num1, num2 = 30, 140

if divisor_sum(num1) * num2 == divisor_sum(num2) * num1:
    print("Yes they are friendly pair")
else:
    print("No they are not friendly pair")


# Method 1 output : Yes they are friendly pair
# Method 2 output : Yes they are friendly pair

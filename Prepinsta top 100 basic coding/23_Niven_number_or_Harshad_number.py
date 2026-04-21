"""
Concept:
A Harshad (Niven) number is a number that is divisible by the sum of its digits.
We extract digits using modulo (%) (n % 10) and add them to get sum.
Then we check if (num % sum == 0). If true, it is a Harshad number.

Example:
18 → 1 + 8 = 9 → 18 % 9 = 0 → Harshad Number.

Program: Check if a Number is Harshad Number
Description:
    Method 1: Extract digits using loop and check divisibility.
    Method 2: Using math.fsum with map for digit sum.
Complexity:
    Method 1: Time O(d) | Space O(1)
    Method 2: Time O(d) | Space O(d)
"""

# Method 1: Iterative Approach
num = 18
n = num

sum = 0

while n > 0:
    last_digit = n % 10
    sum += last_digit
    n = n // 10

if num % sum == 0:
    print(f"{num} is Harshad number")
else:
    print(f"{num} is not Harshad number")


# Method 2: Using math.fsum
import math

number = 19

digit_sum = int(math.fsum(map(int, str(number))))

if number % digit_sum == 0:
    print(f"{number} is Harshad number")
else:
    print(f"{number} is not Harshad number")


# Method 1 output : 18 is Harshad number
# Method 2 output : 19 is not Harshad number

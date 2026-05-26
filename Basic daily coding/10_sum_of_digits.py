"""
Concept:
The sum of digits of a number is obtained by repeatedly extracting the last digit
using the modulo operator (%) (digits % 10) -> gives remainder which is last digit
 and adding it to a running total (sum = sum + last_digit, then removing the
last digit using integer division (//) -> number = number // 10.

Program: Find Sum of Digits of a Number
Description:
    Method 1: Iterative approach using modulo and division.
    Method 2: Using Python built-in functions and string conversion.
Complexity:
    Method 1: Time O(d) | Space O(1)
    Method 2: Time O(d) | Space O(d)
"""

# Method 1: Iterative Approach logic based
number = 1246246
n = number

sum = 0

while n > 0:
    last_digit = n % 10
    sum += last_digit
    n = n // 10

print(f"The sum of {number} is {sum}")


# Method 2: Using built-in functions
number = 1246246

result = sum(int(digit) for digit in str(number))

print(f"Method 2: The sum of {number} is {result}")

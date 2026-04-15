"""
Concept:
An Armstrong number is a number that is equal to the sum of its digits raised
to the power of the total number of digits.
We extract each digit using modulo (%) (temp % 10), then raise it to the power
of number of digits (last_digit ** number_length) and add to result.
Integer division (//) removes the last digit (temp = temp // 10).

Program: Check if a Number is Armstrong
Description:
    Method 1: Extract digits and compute power sum using loop.
    Method 2: Using Python built-in functions for optimized computation.
Complexity:
    Method 1: Time O(d) | Space O(1)
    Method 2: Time O(d) | Space O(d)
"""

# Method 1: Iterative Approach
number = 153
temp = number

number_length = len(str(number))

armstrong_result = 0

while temp > 0:
    last_digit = temp % 10
    armstrong_result += last_digit ** number_length
    temp = temp // 10

if number == armstrong_result:
    print(f"The number {number} is an armstrong number")
else:
    print(f"The number {number} is not an armstrong number")


# Method 2: Using built-in sum (intentionally i have given wrong input (Code is correct))
number = 123

result = sum(int(digit) ** len(str(number)) for digit in str(number))

if number == result:
    print(f"The number {number} is an armstrong number")
else:
    print(f"The number {number} is not an armstrong number")


# Method 1 output : The number 153 is an armstrong number
# Method 2 output : The number 123 is not an armstrong number
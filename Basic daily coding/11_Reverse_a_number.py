"""
Concept:
Reversing a number is done by extracting digits from right to left and building
a new number by shifting existing digits left and appending the extracted digit.
Using modulo (%) gives the last digit (n % 10), and multiplying the reversed number
by 10 shifts its digits left (reversed * 10), then we add the last digit.
Integer division (//) removes the last digit (n = n // 10).

Program: Reverse a Number
Description:
    Method 1: Iterative approach using modulo and division.
    Method 2: Using Python slicing after converting number to string.
Complexity:
    Method 1: Time O(d) | Space O(1)
    Method 2: Time O(d) | Space O(d)
"""

# Method 1: Iterative Approach
number = 12345
n = number

reversed = 0

while n > 0:
    last_digit = n % 10
    reversed = reversed * 10 + last_digit
    n = n // 10

print(f"The input number {number} reversed is {reversed}")


# Method 2: Using string slicing
number = 12345

reversed_num = int(str(number)[::-1])

print(f"Method 2: The input number {number} reversed is {reversed_num}")

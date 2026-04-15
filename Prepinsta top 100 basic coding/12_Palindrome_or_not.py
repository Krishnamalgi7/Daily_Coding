"""
Concept:
A number is a palindrome if it reads the same forward and backward.
We reverse the number using modulo (%) to extract the last digit (temp % 10),
then build the reversed number (result = result * 10 + last_digit) which shifts
digits left and appends the last digit. Integer division (//) removes the last digit
(temp = temp // 10). Finally, compare original and reversed numbers.

Program: Check if a Number is Palindrome
Description:
    Method 1: Reverse the number and compare with original.
    Method 2: Using string reversal.
Complexity:
    Method 1: Time O(d) | Space O(1)
    Method 2: Time O(d) | Space O(d)
"""

# Method 1: Iterative Approach
number = 1221
temp = number

result = 0

if temp == 0:
    print(f"0 is a Palindrome")
else:
    while temp > 0:
        last_digit = temp % 10
        result = result *  10 +  last_digit
        temp = temp // 10

    if number == result:
        print(f"The number {number} is Palindrome")
    else:
        print(f"The number {number} is not a Palindrome")


# Method 2: Using string slicing
number = 1221

if str(number) == str(number)[::-1]:
    print(f"The number {number} is Palindrome")
else:
    print(f"The number {number} is not a Palindrome")


# Method 1 output : The number 1221 is Palindrome
# Method 2 output : The number 1223 is not a Palindrome



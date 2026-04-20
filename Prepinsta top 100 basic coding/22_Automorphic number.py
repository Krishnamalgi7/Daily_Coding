
"""
Concept:
An Automorphic number is a number whose square ends with the same digits as the input number itself.
We square the number and compare the last digits using modulo (%) with increasing powers of 10.
If (square % 10^k == num), where k is number of digits, it is an Automorphic number.

Example:
25 → 25² = 625 → ends with 25 → Automorphic Number

Program: Check if a Number is Automorphic
Description:
    Method 1: Iterative approach increasing divisor (10, 100, ...) and checking suffix.
    Method 2: Direct comparison using number of digits.
Complexity:
    Method 1: Time O(d) | Space O(1)
    Method 2: Time O(1) | Space O(1)
"""

# Method 1: Iterative Approach
num = 25

n = num
square = n**2
divisor = 10
flag = 0

while n > 0:
    res = square % divisor
    if res == num:
        flag = 1
        break
    n = n // 10
    divisor = divisor * 10

if flag == 1:
    print(f"{num} is Automorphic number")
else:
    print(f"{num} is not Automorphic number")


# Method 2: Using digit length way
num = 7

n = num
square = n * n
digits = len(str(n))

if square % (10 ** digits) == num:
    print(f"{num} is Automorphic number")
else:
    print(f"{num} is not Automorphic number")


# Method 1 output : 25 is Automorphic number
# Method 2 output : 7 is not Automorphic number



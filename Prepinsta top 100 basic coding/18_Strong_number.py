"""
Concept:
A Strong number is a number whose sum of factorial of its digits is equal to the number itself.
We extract each digit using modulo (%) (temp % 10), then compute its factorial and add it.
Factorial is calculated using recursion (n * factorial(n-1)).
Finally, compare the sum with the original number.

Program: Check if a Number is Strong Number
Description:
    Method 1: Using recursion to calculate factorial of each digit.
    Method 2: Using Python built-in math.factorial().
Complexity:
    Method 1: Time O(d * n) | Space O(n) (recursion stack)
    Method 2: Time O(d) | Space O(1)
"""

# Method 1: Iterative + Recursion
def factorial_number(n):
    if n == 0:
        return 1
    return n * factorial_number(n-1)

def strong_number(n):
    temp = n
    result = 0
    while temp > 0:
        last_digit = temp % 10
        result = result + factorial_number(last_digit)
        temp //= 10
    return result == n

num = 145

if strong_number(num):
    print(f"{num} is a strong number")
else:
    print(f"{num} is not a strong number")


# Method 2: Using built-in factorial (intentional different input)
import math

number = 123

temp = number
result = 0

while temp > 0:
    digit = temp % 10
    result += math.factorial(digit)
    temp //= 10

if number == result:
    print(f"{number} is a strong number")
else:
    print(f"{number} is not a strong number")


# Method 1 output : 145 is a strong number
# Method 2 output : 123 is not a strong number

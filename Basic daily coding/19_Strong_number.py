"""
Concept:
A Strong number is a number whose sum of factorial of its digits is equal to the number itself.
We extract each digit using modulo (%) (temp % 10), then compute its factorial and add it.
Factorial is calculated using recursion (n * factorial(n-1)).
Finally, compare the sum with the original number.

Program: Check if a Number is Strong Number
Description:
    Method 1: Using recursion to calculate factorial of each digit.
    Method 2: Using string conversion to iterate digits with recursion.
    Method 3: Using Python built-in math.factorial().

Complexity:
    Method 1: Time O(d * n) | Space O(n)
    Method 2: Time O(d * n) | Space O(n)
    Method 3: Time O(d) | Space O(1)

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
    print(f"{num} it's a strong number")
else:
    print(f"{num} it's not a strong number")


# Method 2: Using string iteration + recursion
def factorial_num(n):
    if n == 0:
        return 1
    return n * factorial_num(n-1)


def is_strong_number(n):
    result = 0

    for digit in str(n):
        result += factorial_num(int(digit))

    return result == n

num = 145

if is_strong_number(num):
    print(f"{num} is a Strong Number.")
else:
    print(f"{num} is not a Strong Number.")


# Method 3: Using built-in factorial (intentional different input)
import math

number = 123

temp = number
result = 0

while temp > 0:
    digit = temp % 10
    result += math.factorial(digit)
    temp //= 10

if number == result:
    print(f"{number} it's a strong number")
else:
    print(f"{number} it's not a strong number")




# Method 1 output : 145 it's a strong number
# Method 2 output : 145 is a Strong Number!
# Method 3 output : 123 it's not a strong number


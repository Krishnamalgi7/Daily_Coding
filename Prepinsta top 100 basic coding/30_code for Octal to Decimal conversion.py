"""
Concept:
Octal to Decimal conversion means converting a base-8 number into base-10.
Each digit is multiplied by powers of 8 starting from right (LSB).

Example:
17 → (1×8^1) + (7×8^0) = 8 + 7 = 15

Program: Convert Octal to Decimal
Description:
    Method 1: Iterative approach using modulo and base multiplication.
    Method 2: Using built-in int() with base 8.
Complexity:
    Method 1: Time O(d) | Space O(1)
    Method 2: Time O(d) | Space O(1)
"""

# Method 1: Iterative Approach
num = 17
n = num

res = 0
base = 1

while n > 0:
    rem = n % 10
    res = res + rem * base
    n = n // 10
    base = base * 8

print(f"Octal to Decimal is {res}")


# Method 2: Using built-in int()
octal_str = "25"

decimal = int(octal_str, 8)

print(f"Octal to Decimal is {decimal}")


# Method 1 output : Octal to Decimal is 15
# Method 2 output : Octal to Decimal is 21

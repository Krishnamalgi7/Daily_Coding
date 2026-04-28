"""
Concept:
Hexadecimal to Decimal conversion means converting a base-16 number into base-10.
Digits include 0–9 and A–F (A=10, B=11, ..., F=15).
Each digit is multiplied by powers of 16 starting from right (LSB).

Example:
1A → (1×16^1) + (10×16^0) = 16 + 10 = 26

Program: Convert Hexadecimal to Decimal
Description:
    Method 1: Iterative approach converting each digit and applying base multiplication.
    Method 2: Using built-in int() with base 16.
Complexity:
    Method 1: Time O(d) | Space O(1)
    Method 2: Time O(d) | Space O(1)
"""

# Method 1: Iterative Approach (manual logic)
hex_num = "1A"
n = hex_num

res = 0
base = 1

for ch in reversed(n):
    if '0' <= ch <= '9':
        value = ord(ch) - ord('0')
    else:
        value = ord(ch.upper()) - ord('A') + 10

    res = res + value * base
    base = base * 16

print(f"Hexadecimal to Decimal is {res}")


# Method 2: Using built-in int()
hex_str = "2F"

decimal = int(hex_str, 16)

print(f"Hexadecimal to Decimal is {decimal}")


# Method 1 output : Hexadecimal to Decimal is 26
# Method 2 output : Hexadecimal to Decimal is 47

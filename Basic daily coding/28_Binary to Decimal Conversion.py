"""
Concept:
Binary to Decimal conversion means converting a base-2 number into base-10.
Each digit is multiplied by powers of 2 starting from right (LSB).
We use (rem * base) where base = 2^position and keep increasing base.

Example:
1101 → (1×2^3) + (1×2^2) + (0×2^1) + (1×2^0)
     → 8 + 4 + 0 + 1 = 13

Program: Convert Binary to Decimal
Description:
    Method 1: Iterative approach using modulo and base multiplication.
    Method 2: Using built-in int() with base 2.
    Method 3: Using power calculation with position index.
Complexity:
    Method 1: Time O(d) | Space O(1)
    Method 2: Time O(d) | Space O(1)
    Method 3: Time O(d) | Space O(1)
"""

# Method 1:  Iterative approach using modulo and base multiplication
num = 1101
n = num

res = 0
base = 1

while n > 0:
    rem = n % 10
    res = res + rem * base
    n = n // 10
    base = base * 2

print(f"Binary of {num} to Decimal is {res}")


# Method 2: Using built-in int() function with base 2
binary_str = "1100"
decimal = int(binary_str, 2)
print(f'Binary of {binary_str} to Decimal is {decimal}')


# Method 3: Using index and power method
binary_str = "1010"
decimal = 0

length = len(binary_str)

for i in range(length):
    digit = int(binary_str[length - 1 - i])
    decimal += digit * (2 ** i)

print(f"Binary of {binary_str} to Decimal is {decimal}")


# Method 1 output : Binary of 1101 to Decimal is 13
# Method 2 output : Binary of 1100 to Decimal is 12
# Method 3 output : Binary of 1010 to Decimal is 10


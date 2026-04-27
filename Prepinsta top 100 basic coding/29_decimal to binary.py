"""
Concept:
Decimal to Binary conversion means converting a base-10 number into base-2.
We repeatedly divide the number by 2 and store the remainders.
The binary number is formed by reading remainders in reverse order.

Example:
13 → 13/2=6 r1 → 6/2=3 r0 → 3/2=1 r1 → 1/2=0 r1
→ Binary = 1101

Program: Convert Decimal to Binary
Description:
    Method 1: Iterative approach using division by 2 and building result.
    Method 2: Using built-in bin() function.
Complexity:
    Method 1: Time O(log n) | Space O(log n)
    Method 2: Time O(log n) | Space O(log n)
"""

# Method 1: Iterative Approach
num = 13
n = num

binary = ""

if n == 0:
    binary = "0"
else:
    while n > 0:
        rem = n % 2
        binary = str(rem) + binary
        n = n // 2

print(f"Decimal to Binary is {binary}")


# Method 2: Using built-in bin()
num = 10

binary = bin(num)[2:]

print(f"Decimal to Binary is {binary}")


# Method 1 output : Decimal to Binary is 1101
# Method 2 output : Decimal to Binary is 1010



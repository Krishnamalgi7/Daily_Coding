"""
Concept:
Decimal to Octal conversion means converting a base-10 number into base-8.
We repeatedly divide the number by 8 and store the remainders.
The octal number is formed by reading remainders in reverse order.

Example:
15 → 15/8=1 r7 → 1/8=0 r1
→ Octal = 17

Program: Convert Decimal to Octal
Description:
    Method 1: Iterative approach using division by 8 and building result.
    Method 2: Using built-in oct() function.
Complexity:
    Method 1: Time O(log n) | Space O(log n)
    Method 2: Time O(log n) | Space O(log n)
"""

# Method 1: Iterative Approach
num = 15
n = num

octal = ""

if n == 0:
    octal = "0"
else:
    while n > 0:
        rem = n % 8
        octal = str(rem) + octal
        n = n // 8

print(f"Decimal to Octal is {octal}")


# Method 2: Using built-in oct()
num = 20

octal = oct(num)[2:]

print(f"Decimal to Octal is {octal}")


# Method 1 output : Decimal to Octal is 17
# Method 2 output : Decimal to Octal is 24

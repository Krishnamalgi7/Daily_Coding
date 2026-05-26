"""
Concept:
We replace every 0 in a number by extracting digits using modulo (%) and rebuilding the number.
While extracting digits (n % 10), if digit is 0 → replace with 1.
Then reconstruct the number using place values (base = base * 10).

Example:
12090 → digits → 1,2,0,9,0 → replace → 1,2,1,9,1 → result = 12191

Program: Replace 0's with 1 in a Number
Description:
    Method 1: Using while loop and digit reconstruction.
    Method 2: Using string replacement (built-in).
Complexity:
    Method 1: Time O(d) | Space O(1)
    Method 2: Time O(d) | Space O(d)
"""

# Method 1: While loop manual logic
num = 12090
n = num

res = 0
base = 1

while n > 0:
    digit = n % 10
    if digit == 0:
        digit = 1
    res = res + digit * base
    base = base * 10
    n = n // 10

print(f"Number after replacing 0's with 1 is {res}")

# Method 2: Using string replace
num = 1002

result = int(str(num).replace('0', '1'))

print(f"Number after replacing 0's with 1 is {result}")


# Method 1 output : Number after replacing 0's with 1 is 12191
# Method 2 output : Number after replacing 0's with 1 is 1112


"""
Concept:
LCM (Least common multiple) is the smallest number that is divisible by both numbers.
We can use the relationship:
LCM × HCF = num1 × num2
So, LCM = (num1 * num2) // HCF

Example:
36, 60 → HCF = 12  
LCM = (36 × 60) / 12 = 180

Program: Find LCM of Two Numbers
Description:
    Method 1: Compute HCF using iteration, then calculate LCM.
    Method 2: Using math.gcd() built-in function.
Complexity:
    Method 1: Time O(n) | Space O(1)
    Method 2: Time O(log n) | Space O(1)
"""

# Method 1: Using HCF
num1 = 36
num2 = 60

hcf = 1
if num2 > num1:
    mn = num2
else:
    mn = num1

for i in range(1, mn+1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

lcm = (num1 * num2) // hcf

print(f"The LCM of {num1} and {num2} is: {lcm}")


# Method 2: Using built-in gcd (intentional different input)
import math

a = 12
b = 15

lcm = (a * b) // math.gcd(a, b)

print(f"The LCM of {a} and {b} is: {lcm}")

# o/p:
# Method 1 : The LCM of 36 and 60 is: 180
# Method 2 : The LCM of 12 and 15 is: 60

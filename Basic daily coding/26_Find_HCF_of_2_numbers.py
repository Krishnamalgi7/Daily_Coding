"""
Concept:
HCF (Highest Common Factor) or GCD (Greatest Common Divisor) is the largest number
that divides both numbers exactly.
We check common divisors using (num1 % i == 0 and num2 % i == 0) and keep updating HCF.

Example:
36 → Factors: 1,2,3,4,6,9,12,18,36  
60 → Factors: 1,2,3,4,5,6,10,12,15,20,30,60  
Common → 1,2,3,4,6,12 → HCF = 12

Program: Find HCF of Two Numbers
Description:
    Method 1: Iterative approach checking all numbers from 1 to max(num1, num2).
    Method 2: Using Euclidean Algorithm (optimized).
Complexity:
    Method 1: Time O(n) | Space O(1)
    Method 2: Time O(log n) | Space O(1)
"""

# Method 1: Iterative Approach
num1 = 36
num2 = 60

hcf = 1
if num1 > num2:
    mn = num1
else:
    mn = num2

for i in range(1, mn+1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print(f"The HCF of {num1} and {num2} is: {hcf}")


# Method 2: Euclidean Algorithm
a = 48
b = 18

while b != 0:
    a, b = b, a % b

print(f"The HCF of 48 and 18 is: {a}")

# Outputs of both method:
# Method 1 : The HCF of 36 and 60 is: 12
# Method 2 : The HCF of 48 and 18 is: 6


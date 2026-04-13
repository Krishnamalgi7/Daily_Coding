"""
Program: Sum of Numbers in a Range
Description:
    Method 1: Iterative approach using a 'for' loop to traverse from num1 to num2.
    Method 2: Mathematical approach using the difference of two sum series.
Complexity:
    Method 1 (Loop): Time O(n) | Space O(1)
    Method 2 (Formula): Time O(1) | Space O(1)
"""

num1 = int(input("Enter a number: "))
num2 = int(input("Enter second number : "))

# Method 1: Iterative Approach
sum = 0
for number in range(num1, num2 + 1):
    sum += number

print(f'The range sum (Iterative) is {sum}')

# Method 2: Mathematical Approach
# Using the sum of N natural numbers formula: (n * (n + 1)) // 2
sum = (num2 * (num2 + 1) // 2) - (num1 * (num1 - 1) // 2)

print(f'The range sum (Formula) is {sum}')
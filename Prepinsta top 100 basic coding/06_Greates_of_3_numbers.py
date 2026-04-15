"""
Program: Greatest of Three Numbers
Description:
    Method 1: Using logical AND with if-elif-else statements.
    Method 2: Using Python's built-in max() function for multiple arguments.
Complexity:
    Method 1: Time O(1) | Space O(1)
    Method 2: Time O(1) | Space O(1)
"""
# Method 1: Comparison Logic
num1 = 60
num2 = 56
num3 = 87

if num1 >= num2 and num1 >= num3:
    print(f'The greatest number is {num1}')
elif num2 >= num1 and num2 >= num3:
    print(f'The greatest number is {num2}')
else:
    print(f'The greatest number is {num3}')

# Method 2: Using built-in max() function
# max() can take multiple variables separated by commas
greatest = max(num1, num2, num3)
print(f'The greatest number using max() is {greatest}')
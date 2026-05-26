"""
Program: Greatest of Two Numbers
Description:
    Method 1: Standard if-else conditional logic.
    Method 2: Using Python's built-in max() function.
Complexity:
    Method 1: Time O(1) | Space O(1)
    Method 2: Time O(1) | Space O(1)
"""
# Method 1: Standard If-Else
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(f'{num1} is the greatest')
else:
    print(f'{num2} is the greatest')

# Method 2: Using built-in max() function
greatest = max(num1, num2)
print(f'The greatest number using max() is {greatest}')
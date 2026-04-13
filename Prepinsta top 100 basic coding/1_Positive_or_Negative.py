"""
Program: Check if a Number is Positive, Negative, or Zero
Description: Takes an integer input and uses conditional logic to determine its sign.
Complexity: Time O(1) | Space O(1)
"""

num = int(input("Enter a number : "))

if num > 0:
    print('positive number ')
elif num < 0:
    print('Negative')
else:
    print('Zero')
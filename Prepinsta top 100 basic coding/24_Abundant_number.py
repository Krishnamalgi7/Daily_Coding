"""
Concept:
An Abundant number is a number whose sum of proper divisors (excluding itself)
is greater than the number. We find divisors using (n % i == 0) and add them.
If the total sum > number, it is an Abundant number.

Example:
12 → Factors: 1, 2, 3, 4, 6 → Sum = 16 > 12 → Abundant Number

Program: Check if a Number is Abundant Number
Description:
    Method 1: Iterative approach checking divisors from 1 to n-1.
    Method 2: Using list + sum() to collect and evaluate divisors.
Complexity:
    Method 1: Time O(n) | Space O(1)
    Method 2: Time O(n) | Space O(n)
"""

# Method 1: Iterative Approach
num = 12
n = num

sum = 1

for i in range(2, n):
    if (n % i == 0):
        sum = sum + i

if (sum > n):
    print(n, 'is Abundant Number')
else:
    print(n, 'is not Abundant Number')


# Method 2: Using list + sum()
number = 16

if number <= 0:
    print("Please enter a positive number")
else:
    arr = []

    for index in range(1, number):
        if number % index == 0:
            arr.append(index)

    total_sum = sum(arr)

    if total_sum > number:
        print(number, 'is an Abundant Number')
    else:
        print(number, 'is not an Abundant Number')


# Method 1 output : 12 is Abundant Number
# Method 2 output : 16 is not an Abundant Number


"""
Program: Check if a Year is a Leap Year
Description:
    Method 1: Custom function using logic: (year%4==0 and year%100!=0) or (year%400==0).
    Method 2: Using Python's built-in calendar.isleap() function.
Complexity:
    Method 1: Time O(1) | Space O(1)
    Method 2: Time O(1) | Space O(1)
"""
# Your Method 1: Using logic
import calendar

def Leapornot(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

year = 2024

print(f"{year} is {'Leap Year' if Leapornot(year) else 'Not a Leap Year'}")

# Method 2: Using built-in calendar module
if calendar.isleap(year):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not a Leap Year")
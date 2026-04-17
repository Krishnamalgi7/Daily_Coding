"""
Concept:
Power of a number means multiplying the base number repeatedly by itself.
We use a loop to multiply the number (result = result * num) for given power times.
If power is negative, we convert it using abs(power) and later take reciprocal if needed.

Program: Calculate Power of a Number
Description:
    Method 1: Iterative approach using loop multiplication.
    Method 2: Using Python built-in pow() function.
Complexity:
    Method 1: Time O(n) | Space O(1)
    Method 2: Time O(log n) | Space O(1)
"""

# Method 1: Iterative Approach
num = 10
power = 2

result = 1

abs_power = abs(power)

if num == 0:
    print("Cannot find power of 0")
elif num == 1:
    print(f"1 to the Power is {result}")
else:
    for i in range(abs_power):
        result = result * num
    print(f"The Power of {num} to the {power} is {result}")


# Method 2: Using built-in pow()
num = -10
power = 2

if num == 0 and power < 0:
    print("Error: Cannot raise zero to a negative power (division by zero).")
else:
    result = pow(num, power)
    print(f"{num} to the power of {power} is {result}")


# Method 1 output : The Power of 10 to the 2 is 100
# Method 2 output : The Power of -10 to the 2 is 100

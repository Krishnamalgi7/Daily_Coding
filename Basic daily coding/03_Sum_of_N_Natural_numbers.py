"""
Program: Sum of First N Natural Numbers
Description:
    Method 1: Iterative approach using a 'for' loop to accumulate the sum.
    Method 2: Mathematical formula [n*(n+1)/2] for constant time calculation.
Complexity:
    Method 1 (Loop): Time O(n) | Space O(1)
    Method 2 (Formula): Time O(1) | Space O(1)
"""
# Method 1: Iterative Approach
N = int(input("Enter a number : "))

sum = 0
for num in range(1, N + 1):
    sum = sum + num

print(f"The sum (Iterative) of {N} is {sum}")

# Method 2: Mathematical Approach
sum = (N * (N + 1)) // 2

print(f"The sum (Formula) of {N} is {sum}")
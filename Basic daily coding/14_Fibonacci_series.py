"""
Concept:
Fibonacci sequence is a series where each number is the sum of the two preceding ones.
We start with 0 and 1, then generate next numbers using (c = a + b).
After generating a number, we shift values (a = b, b = c) to continue the sequence.

Program: Generate Fibonacci Series
Description:
    Method 1: Iterative approach using loop and variable shifting.
    Method 2: Using function to store and return sequence.
    Method 3: Using recursion with caching (lru_cache).
Complexity:
    Method 1: Time O(n) | Space O(1)
    Method 2: Time O(n) | Space O(n)
    Method 3: Time O(n) | Space O(n)
"""

# Method 1: Iterative Approach
N = 10
a = 0
b = 1

if N <= 0:
    print("Please enter a positive integer.")
elif N == 1:
    print(f"Fibonacci series: {a}")
else:
    print("Fibonacci series:", a, b, end=" ")

    for i in range(2, N):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
print()

# Method 2: Using function
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

num = 10
print("Fibonacci series:", *fibonacci(num))


# Method 3: Recursion + caching
from functools import lru_cache

@lru_cache(None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

N = 10
result3 = [fib(i) for i in range(N)]

print("Fibonacci series:", *result3)


# Method 1 output : Fibonacci series: 0 1 1 2 3 5 8 13 21 34
# Method 2 output : Fibonacci series: 0 1 1 2 3 5 8 13 21 34
# Method 3 output : Fibonacci series: 0 1 1 2 3 5 8 13 21 34
"""
Concept:
Pascal's Triangle is formed by placing 1 at the beginning and end of each row.
Every middle element is the sum of the two elements directly above it:
row[j] = prev_row[j-1] + prev_row[j]

Example:
n = 5

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

Program: Print Pascal's Triangle
Description:
    Method 1: Build each row using previous row values.
    Method 2: Using nCr (Combination Formula).
Complexity:
    Method 1: Time O(n²) | Space O(n)
    Method 2: Time O(n²) | Space O(1)
"""
from email.header import BSPACE

# Method 1: Using previous row
n = 5

row = [1]

for i in range(n):
    print(" " * (n - i), end=" ")

    for num in row:
        print(num, end=" ")

    print()

    new_row = [1]

    for j in range(len(row)-1):
        new_row.append(row[j] + row[j+1])

    new_row.append(1)

    row = new_row

print()

# Method 2: Using nCr Formula
n = 4

for i in range(n):
    value = 1

    for j in range(i + 1):
        print(value, end=" ")

        value = value * (i - j) // (j + 1)

    print()


# Method 1 output :
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1

# Method 2 o/p:
# 1
# 1 1
# 1 2 1
# 1 3 3 1



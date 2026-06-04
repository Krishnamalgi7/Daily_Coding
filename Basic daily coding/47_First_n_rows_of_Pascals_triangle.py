"""
Concept:
Pascal's Triangle starts with [1].
Every new row begins and ends with 1.
The middle elements are formed by adding adjacent elements from the previous row.

Example:
Previous Row : [1, 3, 3, 1]

New Row:
1
1+3 = 4
3+3 = 6
3+1 = 4
1

Result: [1, 4, 6, 4, 1]

Program: Print Pascal's Triangle
Description:
    Method 1: Build each row using adjacent elements of the previous row.
    Method 2: Using nCr (Combination Formula).
Complexity:
    Method 1: Time O(n²) | Space O(n)
    Method 2: Time O(n²) | Space O(1)
"""

# Method 1: Using previous row
n = 5

row = [1]

for i in range(n):
    print(" " * (n - i), end=" ")

    for num in row:
        print(num, end=" ")

    print()

    new_row = [1]

    for j in range(len(row) - 1):
        new_row.append(row[j] + row[j + 1])

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
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1

# Method 2 output :
# 1
# 1 1
# 1 2 1
# 1 3 3 1


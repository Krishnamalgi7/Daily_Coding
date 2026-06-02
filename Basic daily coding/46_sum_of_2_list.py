"""
Concept:
To add two lists element-wise, we add elements at the same index position.
For each index i, we calculate:
lst1[i] + lst2[i]
and store the result in a new list.

Example:
[1, 2, 3] + [4, 5, 6]
→ [5, 7, 9]

Program: Sum of Two Lists
Description:
    Method 1: Iterative approach using loop and index.
    Method 2: Using zip() and list comprehension.
Complexity:
    Method 1: Time O(n) | Space O(n)
    Method 2: Time O(n) | Space O(n)
"""

# Method 1: Iterative Approach
def sum_of_2_list(lst1, lst2):
    new_lst = []
    n = len(lst1)

    for i in range(n):
        total = lst1[i] + lst2[i]
        new_lst.append(total)

    return new_lst


num1 = [6, -5, 4, 2, 10, 91, -75, 49, 9]
num2 = [4, 1, 54, 76, 41, 85, 3, 44, 2]

print(sum_of_2_list(num1, num2))


# Method 2: Using zip()
num1 = [1, 2, 3, 4]
num2 = [5, 6, 7, 8]

result = [a + b for a, b in zip(num1, num2)]

print(result)


# Method 1 output : [10, -4, 58, 78, 51, 176, -72, 93, 11]
# Method 2 output : [6, 8, 10, 12]


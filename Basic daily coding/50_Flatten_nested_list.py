"""
Concept:
Flattening a nested list means converting all nested elements into a single list.
If an element is a list, we recursively process it and add its elements.
Otherwise, we directly add the element to the result.

Example:
[1, 2, [3, 4], [5, [6, 7]]]
→ [1, 2, 3, 4, 5, 6, 7]

Program: Flatten a Nested List
Description:
    Method 1: Using recursion and extend().
    Method 2: Using recursion and list concatenation.
Complexity:
    Method 1: Time O(n) | Space O(n)
    Method 2: Time O(n²) | Space O(n)
"""

# Method 1: Using recursion and extend()
lst = [1, 2, 3, [4, 5, 6, [7, 8, 9]]]

def flatten(lst):
    l = []

    for i in lst:
        if type(i) == list:
            l.extend(flatten(i))
        else:
            l.append(i)

    return l

print(flatten(lst))


# Method 2: Using recursion and concatenation
lst = [10, [20, 30], [40, [50, 60]]]

def flatten_list(lst):
    result = []

    for item in lst:
        if type(item) == list:
            result = result + flatten_list(item)
        else:
            result.append(item)

    return result

print(flatten_list(lst))


# Method 1 output :
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Method 2 output :
# [10, 20, 30, 40, 50, 60]

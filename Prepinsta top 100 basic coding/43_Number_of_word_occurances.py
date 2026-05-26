"""
Concept:
Word frequency means counting how many times each word appears in a sentence.
We split the sentence into words using split(), then store counts in a dictionary.
If a word already exists, increase count; otherwise initialize with 1.

Example:
"hi hello hi"
→ hi: 2
→ hello: 1

Program: Count Frequency of Words in a Sentence
Description:
    Method 1: Using dictionary to manually count words.
    Method 2: Using collections.Counter built-in function.
Complexity:
    Method 1: Time O(n) | Space O(n)
    Method 2: Time O(n) | Space O(n)
"""

# Method 1: Using dictionary
sentence = 'This is to test the occurances of the dictionary where each word is counted so the word count counted.'

sentence = sentence.replace(".", "")

words = sentence.split()

count_dict = {}

for word in words:

    if word in count_dict:
        count_dict[word] += 1

    else:
        count_dict[word] = 1

for key, value in count_dict.items():
    print(f"{key}: {value}")

print()

# Method 2: Using Counter
from collections import Counter

sentence = "python is easy and python is powerful"

words = sentence.split()

freq = Counter(words)

for key, value in freq.items():
    print(f"{key}: {value}")


# Method 1 output :

# This: 1
# is: 2
# to: 1
# test: 1
# the: 3
# occurances: 1
# of: 1
# dictionary: 1
# where: 1
# each: 1
# word: 2
# counted: 2
# so: 1
# count: 1

# Method 2 output :

# python: 2
# is: 2
# easy: 1
# and: 1
# powerful: 1

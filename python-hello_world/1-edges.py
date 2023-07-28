#!/usr/bin/python3
word = "Holberton"

# Getting the first 3 letters using slicing
word_first_3 = word[:3]

# Getting the last 2 letters using slicing
word_last_2 = word[-2:]

# Getting the middle word using slicing
middle_start = (len(word) - 2) // 2
middle_end = middle_start + 2
middle_word = word[middle_start:middle_end]

# Printing the results
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))


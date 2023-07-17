#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HER
# Generate a random signed number between -100 and 100 (inclusive)
number = random.randint(-100, 100)

# Check if the number is positive, negative, or zero and print the result
if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")E

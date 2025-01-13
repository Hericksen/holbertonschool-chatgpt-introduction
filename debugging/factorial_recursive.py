#!/usr/bin/python3
import sys

# Function description:
# This function calculates the factorial of a given non-negative integer `n` using recursion.
def factorial(n):
    # Parameters:
    # n (int): A non-negative integer whose factorial is to be calculated.

    # Returns:
    # (int): The factorial of the integer `n`.
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Taking the input argument from the command line, converting it to an integer,
# and calling the factorial function on it.
f = factorial(int(sys.argv[1]))

# Printing the result of the factorial calculation.
print(f)

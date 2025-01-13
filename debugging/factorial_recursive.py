#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Args:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of n. If n is 0, returns 1 as 0! is defined to be 1.

    Raises:
        ValueError: If n is a negative number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    """
    Entry point of the script. Expects a single command-line argument,
    a non-negative integer, and prints its factorial.
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: ./factorial_recursive.py <non-negative integer>")
        sys.exit(1)

    try:
        # Convert the input to an integer
        num = int(sys.argv[1])
        # Calculate the factorial
        result = factorial(num)
        # Print the result
        print(result)
    except ValueError as e:
        # Handle invalid input (e.g., non-integer or negative input)
        print(f"Error: {e}")
        sys.exit(1)

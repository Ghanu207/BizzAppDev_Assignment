"""
Approach:

- Use a recursive function that prints the current number and then calls itself with the number - 1.
- Base case is when the number reaches 0.
"""
import sys

sys.setrecursionlimit(1100)

def reverse_count(n):
    if n == 0:
        return
    print(n)
    reverse_count(n - 1)

# Call the function
reverse_count(1000)


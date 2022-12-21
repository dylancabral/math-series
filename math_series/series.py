import pytest

def test_one():
    return "goodbye"
def fibonacci(n):
    if n in{0,1}:
        return n
    return fibonacci(n -1) + fibonacci(n-2)

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)

# def sum_series(n, x=0, y=1):
#     """
#     Finds the n-th index of a new sequence that takes the sum of the previous two elements.
#     """
#     if isinstance(n, int) and isinstance(x, int) and isinstance(y, int):
#         if n == 0:
#             return x
#         if n == 1:
#             return y
#         if n > 1:
#             return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)
#         else:
#             return "Please enter a valid input"
#     else:
#         return "Please enter a valid input"
    
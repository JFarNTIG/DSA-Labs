"""This example demonstrates sorting a small list of integers
using bubble sort.

Using the built-in python timeit library, we can time how long it takes
to sort a list.
"""
from timeit import default_timer as timer
from sortlib.bubble import bubble_sort

items = [12, 54, 32, 41, 2, 5, 1, 0]

print("Original list:")
print(items)

start = timer()
bubble_sort(items)
end = timer()
sort_time = end - start

print("Sorted list:")
print(items)

print(f"Time: {sort_time} seconds")
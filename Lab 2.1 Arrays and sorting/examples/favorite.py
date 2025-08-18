"""This example demonstrates sorting according to the user's "favorite"
sorting algorithm, which can be specified in a settings file.
"""
from sortlib.favorite import get_favorite_sort, favorite_sort

items = [24, 21, 1, 2]
favorite_sort(items)

print(items)

print(f"The list was sorted using: {get_favorite_sort()} sort")
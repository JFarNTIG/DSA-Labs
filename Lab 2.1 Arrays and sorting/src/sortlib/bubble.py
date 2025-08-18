from collections.abc import Callable
from typing import List, Any

def bubble_sort(items: List[Any], compare: Callable = lambda x, y: x > y):
    """Sort a list using the bubble sort algorithm.
    
    Args:
        - items: List of items to sort. The list is sorted **in-place**.
        - compare: Comparison function to use when sorting. It should take
          two arguments x and y, and return True if x is greater than y in the
          ordering. By default, uses the > operator.
    """
    n = len(items)
    for i in range(n-1):
        for j in range(n-i-1):
            if compare(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]

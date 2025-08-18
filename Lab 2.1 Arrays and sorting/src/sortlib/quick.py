from collections.abc import Callable
from typing import List, Any

def quick_sort(items: List[Any], compare: Callable = lambda x, y: x > y):
    """Sort a list using the quick sort algorithm.
    
    Args:
        - items: List of items to sort. The list is sorted **in-place**.
        - compare: Comparison function to use when sorting. It should take
          two arguments x and y, and return True if x is greater than y in the
          ordering. By default, uses the > operator.
    """
    raise NotImplementedError("Not implemented")
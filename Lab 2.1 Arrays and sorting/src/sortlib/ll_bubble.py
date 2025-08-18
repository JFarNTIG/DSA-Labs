from collections.abc import Callable
from sortlib.linkedlist import LinkedList

def ll_bubble_sort(items: LinkedList, compare: Callable = lambda x, y: x > y):
    """Sort a LinkedList using the bubble sort algorithm.
    
    Args:
        - items: Linked list of items to sort. The list is sorted **in-place**.
        - compare: Comparison function to use when sorting. It should take
          two arguments x and y, and return True if x is greater than y in the
          ordering. By default, uses the > operator.
    """
    raise NotImplementedError("Not implemented")
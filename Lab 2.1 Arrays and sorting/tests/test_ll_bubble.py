from typing import List, Any
from sortlib.ll_bubble import ll_bubble_sort
from sortlib.linkedlist import LinkedList

def _ll_equals(ll: LinkedList, arr: List[Any]) -> bool:
    for i, item in enumerate(arr):
        if ll[i] != item:
            return False
        
    return True

def test_ll_bubble_empty_array():
    """Test the sorting algorithm on an empty array.
    """
    items = []
    items = LinkedList(items)
    int_greater = lambda x, y: x > y
    ll_bubble_sort(items, int_greater)

    sorted_expected = []

    assert _ll_equals(items, sorted_expected)


def test_ll_bubble_one_element():
    """Test the sorting algorithm on an empty array.
    """
    items = [6]
    items = LinkedList(items)
    int_greater = lambda x, y: x > y
    ll_bubble_sort(items, int_greater)

    sorted_expected = [6]

    assert _ll_equals(items, sorted_expected)


def test_ll_bubble_small_int_array():
    """Test the sorting algorithm with a small array of ints, sorting
    from least to greatest.
    """
    items = [12, 54, 32, 41, 2, 5, 1, 0]
    items = LinkedList(items)
    int_greater = lambda x, y: x > y
    ll_bubble_sort(items, int_greater)

    sorted_expected = [0, 1, 2, 5, 12, 32, 41, 54]

    assert _ll_equals(items, sorted_expected)


def test_ll_bubble_small_int_array_reversed():
    """Test the sorting algorithm with a small array of ints, sorting
    from greatest to least.
    """
    items = [12, 54, 32, 41, 2, 5, 1, 0]
    items = LinkedList(items)
    int_less = lambda x, y: y > x
    ll_bubble_sort(items, int_less)

    sorted_expected = [54, 41, 32, 12, 5, 2, 1, 0]

    assert _ll_equals(items, sorted_expected)
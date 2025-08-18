from sortlib.quick import quick_sort

def test_quick_empty_array():
    """Test the sorting algorithm on an empty array.
    """
    items = []
    int_greater = lambda x, y: x > y
    quick_sort(items, int_greater)

    sorted_expected = []

    assert items == sorted_expected


def test_quick_one_element():
    """Test the sorting algorithm on an empty array.
    """
    items = [6]
    int_greater = lambda x, y: x > y
    quick_sort(items, int_greater)

    sorted_expected = [6]

    assert items == sorted_expected


def test_quick_small_int_array():
    """Test the sorting algorithm with a small array of ints, sorting
    from least to greatest.
    """
    items = [12, 54, 32, 41, 2, 5, 1, 0]
    int_greater = lambda x, y: x > y
    quick_sort(items, int_greater)

    sorted_expected = [0, 1, 2, 5, 12, 32, 41, 54]

    assert items == sorted_expected


def test_quick_small_int_array_reversed():
    """Test the sorting algorithm with a small array of ints, sorting
    from greatest to least.
    """
    items = [12, 54, 32, 41, 2, 5, 1, 0]
    int_less = lambda x, y: y > x
    quick_sort(items, int_less)

    sorted_expected = [54, 41, 32, 12, 5, 2, 1, 0]

    assert items == sorted_expected


def test_quick_small_str_array():
    """Test the sorting algorithm with a small array of strings, sorting in
    alphabetical order (by first letter only).
    """
    items = ["Zanzibar", "Ivory Coast", "Tazmania", "Marshall Islands", "Andorra"]
    first_char_alphabetical = lambda x, y: x[0] > y[0]
    quick_sort(items, first_char_alphabetical)

    sorted_expected = ["Andorra", "Ivory Coast", "Marshall Islands", "Tazmania", "Zanzibar"]

    assert items == sorted_expected

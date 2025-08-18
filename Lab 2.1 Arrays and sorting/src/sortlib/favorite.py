import json
from collections.abc import Callable
from typing import Dict, List, Any
from sortlib.bubble import bubble_sort
from sortlib.insertion import insertion_sort
from sortlib.merge import merge_sort
from sortlib.quick import quick_sort

"""Can be used to obtain a sorting algorithm from its name."""
_NAME_TO_SORT: Dict[str, Callable] = {
    "bubble": bubble_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "quick": quick_sort,
}

def get_favorite_sort() -> str:
    """Get the user's favorite sorting algorithm from the settings file.

    Raises:
        - ValueError if the user has no favorite sorting algorithm set.
    """
    with open("sort_settings.json") as settings_file:
        settings = json.load(settings_file)

    favorite = settings.get("favorite_sort")
    if favorite is None:
        raise ValueError("No favorite sorting algorithm found!")
    
    return favorite


def favorite_sort(items: List[Any], compare: Callable = lambda x, y: x > y):
    """Sort a list. Uses the user's favorite sorting algorithm,
    determined from their settings.

    Raises:
        - NotImplementedError if the user specified a sorting algorithm we don't
          recognize.
    """
    favorite = get_favorite_sort()

    sort = _NAME_TO_SORT.get(favorite)
    if sort is None:
        raise NotImplementedError(f"No such sorting algorithm `{sort}`")

    sort(items, compare)
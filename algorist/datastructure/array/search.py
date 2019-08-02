from typing import List, Any


def linear(arr: List[Any], key: Any):
    """
    Linear Search on Array

    Args:
        arr: array for searching
        key: key to be found

    Returns:
        -1 if key not found else index
    """
    for idx, num in enumerate(arr):
        if num == key:
            return idx
    return -1

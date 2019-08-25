from algorist.datastructure.heap.heap import MaxHeap, MinHeap
from algorist.helper import identity
from typing import List, Any, Callable
from math import inf


def heapsort(arr: List[Any], reverse: bool = False, key: Callable[[Any], Any] = identity) -> List[Any]:
    """
    Unstable Heap sort

    Args:
        arr: List to be sorted
        reverse: Decreasing sort to be performed
        key: A callable to be used for sorting

    Returns:
        sorted array
    """
    if reverse:
        heap = MaxHeap.build_heap(arr, key=key)
    else:
        heap = MinHeap.build_heap(arr, key=key)

    return [heap.pop() for _ in range(len(arr))]


def is_sorted(arr: List[float]) -> bool:
    return all(x <= y for x, y in zip(arr[:], arr[1:]))


def _flip(arr: List[float], until: int):
    i = 0
    j = until
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


def pancakesort(arr: List[float]):
    """
    Sorts an array inplace
    Args:
        arr: List to be sorted
    """
    size = len(arr)
    while size > 1:

        # Find max
        max_ = -inf
        max_idx = -1
        for idx, val in enumerate(arr[:size]):
            if val > max_:
                max_, max_idx = val, idx

        # 2 Flips to put max at last position
        # First Flip, to bring at first position
        _flip(arr, max_idx)
        # Second Flip to bring max at last position
        _flip(arr, size - 1)
        size -= 1

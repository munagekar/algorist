from math import inf
from typing import List, Any, Callable

from algorist.datastructure.heap.heap import MaxHeap, MinHeap
from algorist.helper import identity


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


def pancakesort(arr: List[float]) -> List[float]:
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
    return arr


def insertionsort(arr: List[float]) -> List[float]:
    """
    Sort an array inplace
    Args:
        arr: List of numbers to be sorted
    """
    for j in range(1, len(arr)):
        temp = arr[j]
        i = j
        while i >= 1 and temp < arr[i - 1]:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = temp
    return arr


def _merge(arr: List[float], left: int, mid: int, right: int):
    if left >= right:
        return
    arr1 = arr[left : mid + 1]
    arr2 = arr[mid + 1 : right + 1]
    len1 = mid - left + 1
    len2 = right - mid
    l, r = 0, 0
    p = left
    while l < len1 and r < len2:
        if arr1[l] <= arr2[r]:
            arr[p] = arr1[l]
            l += 1
        else:
            arr[p] = arr2[r]
            r += 1
        p += 1

    while l < len1:
        arr[p] = arr1[l]
        l += 1
        p += 1
    while r < len2:
        arr[p] = arr2[r]
        r += 1
        p += 1


def mergesort(arr: List[float]) -> List[float]:
    """
    Sort an array inplace
    Args:
        arr: List of numbers to be sorted
    """
    n = len(arr)
    size = 1
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min(left + 2 * size - 1, n - 1)
            _merge(arr, left, mid, right)
        size *= 2
    return arr


def bubblesort(arr: List[float]) -> List[float]:
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(n - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

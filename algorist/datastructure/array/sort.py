from algorist.datastructure.heap.heap import MaxHeap, MinHeap
from algorist.helper import identity
from typing import List, Any, Callable


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

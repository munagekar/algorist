# Binary Heap
from typing import List, Callable, Any

from algorist.helper import identity, negate_func


# Reference : https://prgwonders.blogspot.com/2015/12/max-heap-in-python.html
class Heap:
    def __init__(self, key: Callable[[Any], Any] = identity):
        """
        Max Heap Datastructure
        """
        self._heap = [0]

        self._key = key

    @classmethod
    def build_heap(cls, arr: List[Any], key: Callable[[Any], Any] = identity):
        h = Heap(key)
        n = len(arr)
        h._heap = [n] + arr
        for i in range(n // 2, 0, -1):
            h._heapify(i)
        return h

    def top(self) -> Any:
        if self._heap[0] < 1:
            raise IndexError("EmptyHeap. No value at the top")
        return self._heap[1]

    def pop(self) -> Any:
        top = self.top()
        self._heap[1] = self._heap[self._heap[0]]
        self._heap[0] -= 1
        self._heapify(1)
        self._heap.pop()
        return top

    def insert(self, value: Any):
        self._heap[0] += 1
        # Just Extend the list
        self._heap.append(None)
        i = self._heap[0]
        p = i // 2
        # Bubble up
        while p >= 1 and self._key(self._heap[p]) < self._key(value):
            self._heap[i] = self._heap[p]
            i >>= 1
            p >>= 1
        self._heap[i] = value

    def _heapify(self, i: int):
        if i == 0:
            raise ValueError(f"i={i} cannot be 0")
        n = self._heap[0]
        left_child = 2 * i
        right_child = 2 * i + 1

        largest = i
        if left_child <= n:
            if right_child <= n:
                largest = max(i, left_child, right_child, key=lambda x: self._key(self._heap[x]))
            else:
                largest = max(i, left_child, key=lambda x: self._key(self._heap[x]))

        if largest != i:
            self._heap[i], self._heap[largest] = self._heap[largest], self._heap[i]
            self._heapify(largest)


# Alias
MaxHeap = Heap


class MinHeap(Heap):
    def __init__(self, key: Callable[[Any], Any] = identity):
        key = negate_func(key)
        super().__init__(key)

    @classmethod
    def build_heap(cls, arr: List[float], key=identity):
        h = MinHeap(key)
        key = negate_func(key)
        h._heap = super().build_heap(arr, key)._heap
        return h

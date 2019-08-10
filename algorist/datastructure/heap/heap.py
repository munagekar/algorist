# Binary Heap
from typing import List


# Reference : https://prgwonders.blogspot.com/2015/12/max-heap-in-python.html
class Heap:
    def __init__(self):
        """
        Max Heap Datastructure
        """
        self._heap = [0]

    @classmethod
    def build_heap(cls, arr: List[float]):
        h = Heap()
        n = len(arr)
        h._heap = [n] + arr
        for i in range(n // 2, 0, -1):
            h._heapify(i)
        return h

    def top(self) -> float:
        if self._heap[0] < 1:
            raise IndexError("EmptyHeap. No value at the top")
        return self._heap[1]

    def pop(self) -> float:
        if self._heap[0] < 1:
            raise IndexError("Empty Heap. No values to pop")
        top = self._heap[1]
        self._heap[1] = self._heap[self._heap[0]]
        self._heap[0] -= 1
        self._heapify(1)
        self._heap.pop()
        return top

    def insert(self, num: float):
        self._heap[0] += 1
        self._heap.append(None)
        i = self._heap[0]
        p = i // 2
        # Bubble up
        while p >= 1 and self._heap[p] < num:
            self._heap[i] = self._heap[p]
            i >>= 1
            p >>= 1
        self._heap[i] = num

    def _heapify(self, i: int):
        if i == 0:
            raise ValueError(f"i={i} cannot be 0")
        n = self._heap[0]
        left_child = 2 * i
        right_child = 2 * i + 1

        largest = i
        if left_child <= n:
            if right_child <= n:
                largest = max(i, left_child, right_child, key=lambda x: self._heap[x])
            else:
                largest = max(i, left_child, key=lambda x: self._heap[x])

        if largest != i:
            self._heap[i], self._heap[largest] = self._heap[largest], self._heap[i]
            self._heapify(largest)


class MinHeap(Heap):
    def __init__(self):
        super().__init__()

    @classmethod
    def build_heap(cls, arr: List[float]):
        h = MinHeap()
        h._heap = super().build_heap([-x for x in arr])._heap
        return h

    def top(self) -> float:
        return -super().top()

    def pop(self) -> float:
        return -super().pop()

    def insert(self, num: float):
        super().insert(-num)

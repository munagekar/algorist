from algorist.datastructure.heap.heap import Heap, MinHeap


def test_heap():
    arr = [4, 3, 7, 1, 8, 5]
    h = Heap.build_heap(arr)
    assert h._heap == [len(arr), 8, 4, 7, 1, 3, 5]
    assert h.top() == 8
    assert h.pop() == 8
    assert h._heap == [len(arr) - 1, 7, 4, 5, 1, 3]
    h.insert(-2)
    assert h._heap == [len(arr), 7, 4, 5, 1, 3, -2]
    h.insert(25)
    assert h._heap == [len(arr) + 1, 25, 4, 7, 1, 3, -2, 5]


def test_min_heap():
    arr = [2, 4, 5]
    h = MinHeap.build_heap(arr)
    assert h._heap == [len(arr), 2, 4, 5]
    h.insert(10)
    assert h._heap == [len(arr) + 1, 2, 4, 5, 10]
    assert h.top() == 2
    assert h.pop() == 2
    assert h._heap == [len(arr), 4, 10, 5]

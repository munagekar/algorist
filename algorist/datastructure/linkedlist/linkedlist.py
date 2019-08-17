class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListIterator:
    def __init__(self, start):
        self._start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self._start:
            data = self._start.data
            self._start = self._start.next
            return data
        raise StopIteration


class LinkedList:
    def __init__(self):
        self.head = None
        self._len = 0

    def push(self, data):
        self._len += 1
        node = Node(data)
        node.next = self.head
        self.head = node

    def front(self):
        if not self.head:
            return None
        return self.head.data

    def pop(self):
        if not self.head:
            raise IndexError("No element to pop")
        else:
            self._len -= 1
            data = self.head.data
            self.head = self.head.next
            return data

    def reverse(self):
        # First Pointer
        p1 = self.head
        if p1 is None:
            return
        # Second Pointer
        p2 = p1.next
        if p2 is None:
            return
        # First Node will not have a next Pointer
        p1.next = None
        while p2 is not None:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
        self.head = p1

    def __len__(self):
        return self._len

    def __iter__(self):
        return LinkedListIterator(self.head)

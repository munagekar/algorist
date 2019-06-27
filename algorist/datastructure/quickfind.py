"""
Module for Quick Find
Find : O(1)
Join : O(N) where N is number of nodes
Reference : Chapter 1 Algorithms in C Sedgewick
"""


class QuickFind:

    def __init__(self):
        self._mapping = dict()
        self._nodelist = list()

    def add_node(self, n):
        if n in self._mapping:
            return False
        cur_len = len(self._nodelist)
        self._mapping[n] = cur_len
        self._nodelist.append(cur_len)
        return True

    def connected(self, x, y):
        if self.add_node(x) or self.add_node(y):
            return False
        return self._parent(x) == self._parent(y)

    def _parent(self, n):
        return self._nodelist[self._mapping[n]]

    def join(self, x, y):
        self.add_node(x)
        self.add_node(y)
        px = self._parent(x)
        py = self._parent(y)

        for idx, val in enumerate(self._nodelist):
            if val == px:
                self._nodelist[idx] = py

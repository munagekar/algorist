"""
Module for  QuickUnion
Find : 2logN
Join : 1
Reference : Chapter 1 Algorithms in C Sedgewick
"""


class QuickUnion:
    def __init__(self):
        self._mapping = dict()
        self._nodelist = list()
        self._sizelist = list()

    def add_node(self, n):
        """
        Adds a node to the data structure

        Args:
            n: Anything that is hashable

        Returns:
            True if node doesn't already exist else False
        """
        if n in self._mapping:
            return False
        cur_len = len(self._nodelist)
        self._mapping[n] = cur_len
        self._nodelist.append(cur_len)
        self._sizelist.append(1)
        return True

    def connected(self, x, y):
        """
        Adds the nodes if not already present,

        Args:
            x: Node
            y: Node

        Returns:
            True if connected , False otherwise
        """

        newly_added = self.add_node(x)
        newly_added = self.add_node(y) or newly_added
        if newly_added:
            return False
        return self._ancestor(x) == self._ancestor(y)

    def _ancestor(self, n):
        candidate = self._mapping[n]
        while candidate != self._nodelist[candidate]:
            # Other Compression Alternatives
            # https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Find
            # Path Halving Step
            self._nodelist[candidate] = self._nodelist[self._nodelist[candidate]]
            candidate = self._nodelist[candidate]
        return candidate

    def join(self, x, y):
        """
        Connects the nodes if not connected, adds if not in the graph

        Args:
            x: Node
            y: Node

        Returns:
            True if connected , False otherwise
        """
        self.add_node(x)
        self.add_node(y)
        px = self._ancestor(x)
        py = self._ancestor(y)
        sx = self._sizelist[px]
        sy = self._sizelist[py]

        if sx >= sy:
            self._sizelist[px] += sy
            self._nodelist[py] = px
        else:
            self._sizelist[py] += sx
            self._nodelist[px] = py

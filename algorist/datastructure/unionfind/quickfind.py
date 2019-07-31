"""
Module for Quick Find
Find : O(1)
Join : O(N) where N is number of nodes
Reference : Chapter 1 Algorithms in C Sedgewick
"""
from typing import Any


class QuickFind:
    def __init__(self):
        self._mapping = dict()
        self._nodelist = list()

    def add_node(self, n: Any) -> bool:
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
        return True

    def connected(self, x: Any, y: Any) -> bool:
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

    def _ancestor(self, n: Any):
        return self._nodelist[self._mapping[n]]

    def join(self, x: Any, y: Any):
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

        for idx, val in enumerate(self._nodelist):
            if val == py:
                self._nodelist[idx] = px

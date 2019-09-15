from math import log2, ceil, inf
from typing import List, Any, Callable, Tuple
from algorist.helper import identity
from operator import add


class SparseTable:
    def __init__(self, arr: List[Any], func1: Callable[[Any], Any] = identity, func2: Callable[[Any, Any], Any] = min):
        n = len(arr)
        k = ceil(log2(n))
        table = [[None for _ in range(k + 1)] for _ in range(n + 1)]
        self._func = func2
        for i in range(n):
            table[i][0] = func1(arr[i])

        for j in range(1, k + 1):
            diff = 1 << j
            hdiff = diff >> 1
            for i in range(n):
                # Overflow
                if i + diff - 1 >= n:
                    break
                table[i][j] = func2(table[i][j - 1], table[i + hdiff][j - 1])

        self._k = k
        self._table = table
        self._n = n


class RMQ(SparseTable):
    def __init__(self, arr: List[float]):
        super().__init__(arr)

        self._log = [None, 0]
        for i in range(2, self._n + 1):
            self._log.append(self._log[i // 2] + 1)

    def query(self, low, high) -> float:
        k = self._log[high - low + 1]
        return min(self._table[low][k], self._table[high - (1 << k) + 1][k])


class RSQ(SparseTable):
    def __init__(self, arr: List[float]):
        """
        Education purposes. Use cumulative sum or Fenwick instead
        Args:
            arr: List of values
        """
        super().__init__(arr, func2=add)

    def query(self, low, high) -> float:
        val = 0
        for i in range(self._k, -1, -1):
            if low + (1 << i) - 1 <= high:
                val += self._table[low][i]
                low += 1 << i

        return val

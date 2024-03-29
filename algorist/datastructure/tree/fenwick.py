from itertools import accumulate
from operator import add
from typing import List

from algorist.math.bitops import msbit

"""
References: https://www.topcoder.com/community/competitive-programming/tutorials/binary-indexed-trees/
Binary Indexed Tree.
Read Complexity : 0(1)
update : log(n)
cum_sum : log(n)
scale : 0(n)
Memory: 2 * n
"""


class Fenwick:
    def __init__(self, max_idx: int):
        self._max_idx = max_idx
        self._tree = [0] * (max_idx + 1)
        self._freq = [0] * (max_idx + 1)

    @classmethod
    def from_array(cls, arr: List[float]):
        f = cls(len(arr))
        for idx, val in enumerate(arr):
            f.update(idx, val)
        return f

    def update(self, idx: int, val: float):
        idx += 1
        self._freq[idx] += val
        while idx <= self._max_idx:
            self._tree[idx] += val
            idx += idx & -idx

    def cum_sum(self, idx: int) -> float:
        idx += 1
        sum_ = 0
        while idx > 0:
            sum_ += self._tree[idx]
            idx -= idx & -idx
        return sum_

    def read(self, idx):
        idx += 1
        return self._freq[idx]

    def scale(self, c: float):
        self._tree = [i * c for i in self._tree]
        self._freq = [i * c for i in self._freq]

    def ranged_cum_sum(self, low: int, high: int) -> float:
        """
        Get cumulative sum in a range

        Args:
            low: lower limit of range inclusive
            high: higher limit of range inclusive

        Returns:
            ranged cumulative sum between [low,high]
        """
        return self.cum_sum(high) - self.cum_sum(low - 1)

    # Complexity O(n)
    def linear_cum_search(self, cum_freq: float) -> int:
        """
        Works for both negative and non negative. O(n)

        Args:
            cum_freq: Cummulative frequency which is to be found
        Returns:
            idx at which cumulative frequency is first obtained else -1
        """
        for idx, cum in enumerate(accumulate(self._freq[1:], add)):
            if cum_freq == cum:
                return idx
        return -1

    def binary_cum_search(self, cum_freq: float) -> int:
        """
        Works only in non-negative frequency case. O(log n)

        Args:
            cum_freq: cummulative frequency to be found

        Returns:
            the index at which the cumulative frequency is obtained else -1
        """

        bitmask = msbit(self._max_idx)
        idx = 0

        while bitmask != 0:
            mid = idx + bitmask
            bitmask >>= 1
            # Overflow
            if mid > self._max_idx:
                continue
            if self._tree[mid] == cum_freq:
                cum_freq = 0
                idx = mid
                break
            if self._tree[mid] < cum_freq:
                idx = mid
                cum_freq -= self._tree[mid]
        if cum_freq != 0 or idx == 0:
            return -1
        return idx - 1


# 2x lesser space
"""
Read Complexity : 0(log(n))
update : log(n)
cum_sum : log(n)
scale : 0(n)
Memory: 2 * n
"""


class FenwickLowMemory:
    def __init__(self, max_idx: int):
        self._tree = [max_idx] + [0] * max_idx

    def cum_sum(self, idx: int) -> float:
        idx += 1
        sum_ = 0
        while idx > 0:
            sum_ += self._tree[idx]
            idx -= idx & -idx

        return sum_

    def ranged_cum_sum(self, low: int, high: int) -> float:
        return self.cum_sum(high) - self.cum_sum(low - 1)

    @classmethod
    def from_array(cls, arr: List[float]):
        f = cls(len(arr))
        for idx, val in enumerate(arr):
            f.update(idx, val)
        return f

    def update(self, idx: int, val: float):
        idx += 1
        while idx <= self._tree[0]:
            self._tree[idx] += val
            idx += idx & -idx

    def scale(self, c: float):
        self._tree = [i * c for i in self._tree]

    def read(self, idx: int) -> float:
        # Use bit ops to find common point
        idx += 1
        y = idx - 1
        sum_ = self._tree[idx]
        idx -= idx & -idx
        while idx != y:
            sum_ -= self._tree[y]
            y -= y & -y
        return sum_

    def binary_cum_search(self, cum_freq):
        bitmask = msbit(self._tree[0])
        idx = 0
        while bitmask > 0:
            mid = idx + bitmask
            bitmask >>= 1
            if mid > self._tree[0]:
                continue  # avoid overflow
            if cum_freq == self._tree[mid]:
                idx = mid
                cum_freq = 0
            elif cum_freq > self._tree[mid]:
                cum_freq -= self._tree[mid]
                idx += mid
        if cum_freq != 0 or idx == 0:
            return -1
        return idx - 1

    # 0(n)log(n) Super Slow
    def linear_cum_search(self, cum_freq):
        for i in range(self._tree[0]):
            if self.cum_sum(i) == cum_freq:
                return i
        return -1

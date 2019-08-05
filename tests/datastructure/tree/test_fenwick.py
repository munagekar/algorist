from algorist.datastructure.tree.fenwick import Fenwick, FenwickLowMemory
import random
import operator
import itertools


def test_fenwick():
    array = [1, 2, 3, 4]
    f = Fenwick.from_array(array)
    assert f._tree == [0, 1, 3, 3, 10]
    assert f._freq == [0, 1, 2, 3, 4]

    for idx, expected in enumerate(itertools.accumulate(array, operator.add)):
        assert expected == f.cum_sum(idx)

    assert f.linear_cum_search(1) == 0
    assert f.linear_cum_search(3) == 1
    assert f.linear_cum_search(6) == 2
    assert f.linear_cum_search(10) == 3
    assert f.linear_cum_search(-5) == -1

    assert f.ranged_cum_sum(0, 0) == 1
    assert f.ranged_cum_sum(0, 3) == 10
    assert f.ranged_cum_sum(1, 2) == 5
    assert f.ranged_cum_sum(3, 3) == 4
    f.update(3, 6)
    assert f.read(3) == 10
    assert f.ranged_cum_sum(0, 3) == 16
    assert f._freq[4] == 10
    assert f._tree[4] == 16


def test_fenwick_low_mem():
    array = [1, 2, 3, 4]
    f = FenwickLowMemory.from_array(array)
    assert f._tree == [4, 1, 3, 3, 10]

    for idx, expected in enumerate(itertools.accumulate(array, operator.add)):
        assert expected == f.cum_sum(idx)

    assert f.ranged_cum_sum(0, 0) == 1
    assert f.ranged_cum_sum(0, 3) == 10
    assert f.ranged_cum_sum(1, 2) == 5
    assert f.ranged_cum_sum(3, 3) == 4
    f.update(3, 6)
    assert f.read(3) == 10
    assert f.ranged_cum_sum(0, 3) == 16
    assert f._tree[4] == 16

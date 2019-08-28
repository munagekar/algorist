from algorist.datastructure.array.sort import heapsort, is_sorted, pancakesort, insertionsort, mergesort


def test_heapsort():
    inc = [1, 2, 3, 4, 5]
    dec = [5, 4, 3, 2, 1]
    mix = [2, 3, 5, 1, 0]
    for arr in [inc, dec, mix]:
        assert sorted(arr, reverse=True) == heapsort(arr, reverse=True)
        assert sorted(arr) == heapsort(arr)
        assert sorted(arr, reverse=True) == heapsort(arr, key=lambda x: -x)


def test_is_sorted():
    assert is_sorted([1, 2, 3, 4])
    assert not is_sorted([1, 3, 5, 4])
    assert is_sorted([1, 2, 3, 4, 5, 20])


def test_pancakesort():
    arr = [1, 3, 2]
    pancakesort(arr)
    assert arr == [1, 2, 3]

    arr = [1, 2, 2]
    pancakesort(arr)
    assert arr == [1, 2, 2]

    arr = [3, 2, 1]
    pancakesort(arr)
    assert arr == [1, 2, 3]


def test_insertionsort():
    assert is_sorted(insertionsort([1, 2, 3, 4, 5]))
    assert is_sorted(insertionsort([1, 2, 3, 5, 4]))
    assert is_sorted(insertionsort([5, 4, 3, 2, 1]))
    assert is_sorted(insertionsort([1, 5, 4, 2, 3]))


def test_mergesort():
    assert is_sorted(mergesort([1, 2, 3, 4, 5]))
    assert is_sorted(mergesort([1, 2, 3, 5, 4]))
    assert is_sorted(mergesort([5, 4, 3, 2, 1]))
    assert is_sorted(mergesort([1, 5, 4, 2, 3]))

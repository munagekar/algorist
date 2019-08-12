from algorist.datastructure.array.sort import heapsort


def test_heapsort():
    inc = [1, 2, 3, 4, 5]
    dec = [5, 4, 3, 2, 1]
    mix = [2, 3, 5, 1, 0]
    for arr in [inc, dec, mix]:
        assert sorted(arr, reverse=True) == heapsort(arr, reverse=True)
        assert sorted(arr) == heapsort(arr)
        assert sorted(arr, reverse=True) == heapsort(arr, key=lambda x: -x)

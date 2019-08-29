from algorist.datastructure.array.misc import kadane


def test_kadane():
    assert kadane([-2, -3, 4, -1, -2, 1, 5, -3]) == (7, 2, 6)
    assert kadane([-2, -3, -3]) == (-2, 0, 0)
    assert kadane([-2, -3, -1]) == (-1, 2, 2)
    assert kadane([1, 1, 1, 1, 1]) == (5, 0, 4)
    assert kadane([1, 5, -5, 6]) == (7, 0, 3)
    assert kadane([-4, -3, -2, -1]) == (-1, 3, 3)

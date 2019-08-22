from algorist.number.misc import extended_euclidean


def test_extended_euclidean():
    assert extended_euclidean(10, 3) == (1, 1, -3)
    assert extended_euclidean(20, 25) == (5, -1, 1)
    assert extended_euclidean(25, 20) == (5, 1, -1)

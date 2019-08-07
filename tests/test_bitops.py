from algorist.math.bitops import msbit


def test_msbit():
    assert msbit(0) == 0
    assert msbit(2) == 2
    assert msbit(1) == 1
    assert msbit(3) == 2

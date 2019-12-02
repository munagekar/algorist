from algorist.number.misc import extended_euclidean, gcd


def test_extended_euclidean():
    assert extended_euclidean(10, 3) == (1, 1, -3)
    assert extended_euclidean(20, 25) == (5, -1, 1)
    assert extended_euclidean(25, 20) == (5, 1, -1)


def test_gcd():
    assert gcd(10, 100) == 10
    assert gcd(100, 10) == 10
    assert gcd(1, 1) == 1
    assert gcd(7, 3) == 1
    assert gcd(35, 375) == 5

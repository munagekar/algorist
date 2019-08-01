from algorist.number.prime.prime_test import naive


def test_naive():
    assert naive(0) is False
    assert naive(1) is False
    assert naive(2) is True
    assert naive(3) is True
    assert naive(7) is True
    assert naive(15) is False
    assert naive(16) is False

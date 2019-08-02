import bisect

from algorist.number.prime.sieve import lsieve
from algorist.number.prime.sieve import seg_sieve
from algorist.number.prime.sieve import sieve


def test_sieve():
    primes = sieve(23)
    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert primes == expected_primes


def test_lsieve():
    got = lsieve(23)
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert got == expected

    expected = sieve(1003)
    got = lsieve(1003)
    assert expected == got


def test_seg_sieve():
    assert sieve(23) == seg_sieve(23)
    assert sieve(32) == seg_sieve(32)
    assert sieve(1000) == seg_sieve(1000)
    s2000 = sieve(2000)
    expected = s2000[bisect.bisect_left(s2000, 37) :]
    got = seg_sieve(2000, 37)
    assert expected == got

    assert seg_sieve(7, 6) == [7]
    assert seg_sieve(7, 7) == [7]
    assert seg_sieve(29, 27) == [29]
    assert seg_sieve(30, 15) == [17, 19, 23, 29]

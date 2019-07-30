from algorist.number.prime.sieve import eratosthenes
from algorist.number.prime.sieve import linear_eratosthenes


def test_erathosthenes():
    primes = eratosthenes(23)
    expected_primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23])
    for i in range(22):
        if i in expected_primes:
            assert (primes[i])
        else:
            assert (not primes[i])


def test_linear_eratosthenes():
    got = linear_eratosthenes(23)
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert (got == expected)
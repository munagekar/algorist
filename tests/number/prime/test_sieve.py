from algorist.number.prime.sieve import eratosthenes


def test_erathosthenes():
    primes = eratosthenes(23)
    expected_primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23])
    for i in range(22):
        if i in expected_primes:
            assert (primes[i])
        else:
            assert (not primes[i])
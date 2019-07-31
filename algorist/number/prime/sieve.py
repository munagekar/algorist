from typing import List


# Reference : https://www.geeksforgeeks.org/sieve-of-eratosthenes/
# Time Complexity : O(n)log(log(n))
def eratosthenes(high: int) -> List[bool]:
    prime = [True] * (high + 1)
    prime[0] = False
    prime[1] = False

    for i in range(2, high + 1):
        if prime[i]:
            for j in range(i * i, high + 1, i):
                prime[j] = False

    return prime


# Reference: https://www.hackerrank.com/topics/sieve-of-eratosthenes-linear-time
# Time Complexity : O(n)
def linear_eratosthenes(high: int) -> List[int]:
    """
    A modification over eratosthenes which consumes more memory(~32x) but runs linearly

    Args:
       high: maximum value

    Returns:
        primes upto high(included)
    """
    primes = []
    # Prime Factors
    lp = [0] * (high + 1)

    for i in range(2, high + 1):
        if lp[i] == 0:
            # Is prime
            primes.append(i)
            lp[i] = i

        for p in primes:
            target = p * i  # Next Composite Number to remove

            if target > high or lp[i] < p:
                break

            lp[target] = p

    return primes


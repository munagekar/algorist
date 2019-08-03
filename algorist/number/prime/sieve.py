import bisect
from math import sqrt, floor
from typing import List


# Reference : https://www.geeksforgeeks.org/sieve-of-eratosthenes/
# Time Complexity : O(n)log(log(n))
def sieve(high: int) -> List[int]:
    prime = [True] * (high + 1)
    prime[0] = False
    prime[1] = False

    for i in range(2, high + 1):
        if prime[i]:
            for j in range(i * i, high + 1, i):
                prime[j] = False

    return [idx for idx, is_prime in enumerate(prime) if is_prime]


# Reference: https://www.hackerrank.com/topics/sieve-of-eratosthenes-linear-time
# Time Complexity : O(n)
def lsieve(high: int) -> List[int]:
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


# Reference : https://www.geeksforgeeks.org/segmented-sieve/
# Time Complexity : 0(n)log(log n)
def seg_sieve(high: int, low: int = 0) -> List[int]:
    """
    Memory Optimized Sieve to quickly find primes in a range
    Args:
        high: non negative integer
        low: non negative integer

    Returns:
        A list of prime numbers in the range [low,high] both ends inclusive
    """

    if low > high:
        raise ValueError(f"Low={low} must be greater than high={high}")
    # The return list
    primes_in_range = []

    prime_limit = floor(sqrt(high))
    prime_list = sieve(prime_limit)

    if low < prime_limit:
        limit = bisect.bisect_left(prime_list, low)
        primes_in_range.extend(prime_list[limit:])

    # Get Segments
    seg_low = max(prime_limit + 1, low)
    seg_high = min(seg_low + prime_limit - 1, high)
    while seg_low <= high:
        prime_flag = [True] * (seg_high - seg_low + 1)
        for p in prime_list:
            start = seg_low // p * p
            if start < seg_low:
                start += p
            for i in range(start, seg_high + 1, p):
                prime_flag[i - seg_low] = False
        primes_in_range.extend([idx + seg_low for idx, is_prime in enumerate(prime_flag) if is_prime])

        seg_low = seg_high + 1
        seg_high = min(seg_low + prime_limit - 1, high)

    return primes_in_range

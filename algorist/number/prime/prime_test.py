from math import sqrt, floor


# Time Complexity : 0(n ** 0.5)
def naive(n: int) -> bool:
    if n < 2:
        return False
    limit = floor(sqrt(n))
    return all(n % x for x in range(2, limit + 1))

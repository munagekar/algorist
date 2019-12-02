from typing import Callable

from algorist.number.misc import gcd


def rand_func(x: int, pq: int, c: int = 2) -> int:
    """
    A very naive random number generator
    Args:
        x: seed input
        pq: modulo number
        c: constant

    Returns:
        A random number
    """
    return (x * x + c) % pq


def pollard_rho_brent(num: int, x: int = 2, c: int = 2, randomizer: Callable[[int, int, int], int] = rand_func) -> int:
    """
    This algorithms finds one of the divisors for a composite Number. Ensure that the number is not prime
    Args:
        num: The number whose divisor is to be found
        x: a seed number, the initial value to be used
        c: a seed number, the seed constant for the randomizer function
        randomizer: A function which when given an input number x, the modulo number num and c a seed generates the next
            random number

    Returns:
        A divisor of the number
    """

    if num % 2 == 0:
        return 2

    y = randomizer(x, num, c)

    while y != x:

        diff = y - x if y > x else x - y

        g = gcd(diff, num)
        if g > 1:
            return g
        y = randomizer(randomizer(y, num, c), num, c)
        x = randomizer(x, num, c)
        if y == x:
            raise ValueError(f"Cycle Detected with x={x},c={c}")

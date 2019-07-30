from typing import List


# Reference : https://www.geeksforgeeks.org/sieve-of-eratosthenes/
def eratosthenes(high: int) -> List[bool]:
    prime = [True] * (high + 1)
    prime[0] = False
    prime[1] = False

    for i in range(2, high + 1):
        if prime[i]:
            for j in range(i * i, high+1, i):
                prime[j] = False

    return prime



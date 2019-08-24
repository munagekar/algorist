from typing import List


# Bottom Up dp. Complexity NW
def knapsack(weights: List[int], vals: List[int], cap: int):
    n = len(weights)
    table = [[0 for _ in range(cap + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for w in range(cap + 1):
            if i == 0 or w == 0:
                table[i][w] = 0
                continue

            if weights[i - 1] > w:
                table[i][w] = table[i - 1][w]
                continue

            table[i][w] = max(vals[i - 1] + table[i - 1][w - weights[i - 1]], table[i - 1][w])

    return table[n][cap]

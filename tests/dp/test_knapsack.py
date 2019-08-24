from algorist.dp.knapsack import knapsack


def test_knapsack():
    val = [60, 100, 120]
    wt = [10, 20, 30]
    cap = 50
    assert knapsack(wt, val, cap) == 220

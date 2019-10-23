from typing import List
import random
from algorist.datastructure.array.misc import kadane, product_kadane, two_array_median


def test_kadane():
    assert kadane([-2, -3, 4, -1, -2, 1, 5, -3]) == (7, 2, 6)
    assert kadane([-2, -3, -3]) == (-2, 0, 0)
    assert kadane([-2, -3, -1]) == (-1, 2, 2)
    assert kadane([1, 1, 1, 1, 1]) == (5, 0, 4)
    assert kadane([1, 5, -5, 6]) == (7, 0, 3)
    assert kadane([-4, -3, -2, -1]) == (-1, 3, 3)


def product_kadane_dp(arr: List[float]) -> float:
    """
    Solve Kadanes O(n2)
    Returns:
    """
    n = len(arr)
    table = [[0 for _ in range(n)] for _ in range(n)]
    # Initial values
    for idx in range(n):
        table[0][idx] = arr[idx]
    for diff in range(1, n):
        for left in range(0, n - diff):
            table[diff][left] = table[diff - 1][left] * arr[left + diff]
    print(table)
    return max(max(table[i]) for i in range(n))


def test_product_kadane_dp():
    assert product_kadane_dp([0, 0, -20, -1, 0, -1, 0]) == 20
    assert product_kadane_dp([0, 0, -1, 0, -1, 0]) == 0
    assert product_kadane_dp([-1, 0, -1, 0]) == 0
    assert product_kadane_dp([-1]) == -1
    assert product_kadane_dp([1, -2, -3, 0, 7, -8, -2]) == 112
    assert product_kadane_dp([6, -3, -10, 0, 2]) == 180
    assert product_kadane_dp([-1, -3, -10, 0, 60]) == 60
    assert product_kadane_dp([-2, -3, 0, -2, -40]) == 80
    assert product_kadane_dp([-2, -3, 0, -0.001, -40]) == 6


def test_product_kadane():
    assert product_kadane([0, 0, -20, -1, 0, -1, 0]) == 20
    assert product_kadane([0, 0, -1, 0, -1, 0]) == 0
    assert product_kadane([-1, 0, -1, 0]) == 0
    assert product_kadane([-1]) == -1
    assert product_kadane([1, -2, -3, 0, 7, -8, -2]) == 112
    assert product_kadane([6, -3, -10, 0, 2]) == 180
    assert product_kadane([-1, -3, -10, 0, 60]) == 60
    assert product_kadane([-2, -3, 0, -2, -40]) == 80
    assert product_kadane([-2, -3, 0, -0.001, -40]) == 6


def test_product_kadane2():
    bag = [0, 1, 2, 100, -1, -2, -100, -0.25, 0.25, -0.5, 0.5]
    for test_case in range(10000):
        length = random.randint(10, 100)
        li = [random.choice(bag) for _ in range(length)]
        assert product_kadane(li) == product_kadane_dp(li)


def test_two_array_median_odd():
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6, 7]
    assert two_array_median(arr1, arr2) == 4
    arr1 = [4]
    arr2 = [5, 6]
    assert two_array_median(arr1, arr2) == 5
    arr1 = [4]
    arr2 = [2, 5]
    assert two_array_median(arr1, arr2) == 4
    arr1 = [1, 4]
    arr2 = [2, 5]
    assert two_array_median(arr1, arr2) == 3
    arr1 = [1, 4, 7, 9, 10, 13]
    arr2 = [2, 5]
    assert two_array_median(arr1, arr2) == 6

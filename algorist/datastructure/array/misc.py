from statistics import mean
from typing import Tuple, List


# Reference : https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
def kadane(arr: List[float]) -> Tuple[float, int, int]:
    max_sum = arr[0]
    cur_sum = arr[0]
    l = 0
    r = 0
    max_l = l
    max_r = r
    for i, val in enumerate(arr[1:], 1):
        cur_sum += val

        if cur_sum < val:
            l = i
            r = i
            cur_sum = val
        else:
            r += 1

        if max_sum <= cur_sum:
            max_sum = cur_sum
            max_r = r
            max_l = l
    return max_sum, max_l, max_r


def product_kadane(arr: List[float]) -> float:
    neg = arr[0]
    pos = arr[0]
    target = arr[0]

    for val in arr[1:]:
        if val >= 0:
            pos *= val
            pos = max(pos, val)
            neg *= val
        if val < 0:
            pos, neg = neg, pos
            pos *= val
            neg *= val
            neg = min(neg, val)
        target = max(pos, target)

    return target


def two_array_median(arr1, arr2):
    size1 = len(arr1)
    size2 = len(arr2)
    if (size1 + size2) % 2 == 0:
        return _two_array_median_even(arr1, arr2)
    return _two_array_median_odd(arr1, arr2)


def _two_array_median_even(arr1, arr2):
    median_idx = (len(arr1) + len(arr2)) / 2 - 1
    count = 0
    pointer1, pointer2 = 0, 0
    len1, len2 = len(arr1), len(arr2)
    while count != median_idx:
        count += 1
        if arr1[pointer1] <= arr2[pointer2]:
            pointer1 += 1
        else:
            pointer2 += 1
        if pointer1 == len1:
            return mean((arr2[pointer2 + median_idx - pointer1], arr2[pointer2 + median_idx - pointer1 + 1]))
        if pointer2 == len2:
            return mean((arr1[pointer1 + median_idx - pointer2], arr1[pointer1 + median_idx - pointer2 + 1]))

    first, second = arr1[pointer1], arr2[pointer2]
    if first <= second:
        if pointer1 != len1 - 1:
            second = min(second, arr1[pointer1 + 1])
    else:
        if pointer2 != len2 - 1:
            first = min(first, arr2[pointer2 + 1])
    return mean((first, second))


def _two_array_median_odd(arr1, arr2):
    median_idx = (len(arr1) + len(arr2)) // 2
    count = 0
    pointer1, pointer2 = 0, 0
    len1, len2 = len(arr1), len(arr2)
    while count != median_idx:
        count += 1
        if arr1[pointer1] <= arr2[pointer2]:
            pointer1 += 1
        else:
            pointer2 += 1
        if pointer1 == len1:
            return arr2[pointer2 + median_idx - pointer1]
        if pointer2 == len2:
            return arr1[pointer1 + median_idx - pointer2]

    return min(arr1[pointer1], arr2[pointer2])

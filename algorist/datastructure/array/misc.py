from statistics import mean
from typing import Tuple, List
from math import inf


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


def two_array_median_linear(arr1, arr2):
    size1 = len(arr1)
    size2 = len(arr2)
    if (size1 + size2) % 2 == 0:
        return _two_array_median_even(arr1, arr2)
    return _two_array_median_odd(arr1, arr2)


def two_array_median(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    # First Array must be smaller or equal in size
    if l1 > l2:
        return two_array_median(arr2, arr1)
    median_index = (l1 + l2 + 1) // 2
    is_even = True if (l1 + l2) % 2 == 0 else False

    low = 0
    high = l1

    while low <= high:
        # First array is partitioned into 2 parts
        # [:mid1], [:mid1] Pythonic indexing
        mid1 = (low + high) // 2
        # Array 2 is partitioned similarly
        mid2 = median_index - mid1

        arr1_left_last = -inf if mid1 == 0 else arr1[mid1 - 1]
        arr1_right_first = inf if mid1 == l1 else arr1[mid1]
        arr2_left_last = -inf if mid2 == 0 else arr2[mid2 - 1]
        arr2_right_first = inf if mid2 == l2 else arr2[mid2]

        if arr1_left_last <= arr2_right_first and arr1_right_first >= arr2_left_last:
            median1 = max(arr2_left_last, arr1_left_last)
            if not is_even:
                return median1
            median2 = min(arr1_right_first, arr2_right_first)
            return mean((median1, median2))

        if arr1_left_last > arr2_right_first:
            high = mid1 - 1
        else:
            low = mid1 + 1


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

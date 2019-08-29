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

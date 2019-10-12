from typing import List


# Reference : https://www.youtube.com/watch?v=CpZh4eF8QBw
def cal_z(text) -> List[int]:
    """
    Computes Z array, ie length of longest substring begining at each index which is prefix of the string
    Returns:
        List of length(text) with z values
    """
    l = len(text)
    z = [0] * l
    k = 1
    left = 0
    right = 0
    while k < l:
        if k > right:
            right = k
            left = k

            while right < l and text[right - left] == text[right]:
                right += 1
            z[k] = right - left
            right -= 1
        else:
            k1 = k - left
            if z[k1] < right - k + 1:
                z[k] = z[k1]
            else:
                left = k
                while right < l and text[right - left] == text[right]:
                    right += 1
                z[k] = right - left
                right -= 1

        k += 1

    return z


def substring_z(text: str, pat: str) -> List[int]:
    doc = pat + "$" + text
    z = cal_z(doc)
    l = len(pat)
    adjust = len(pat) + 1
    return [idx - adjust for idx, val in enumerate(z) if val == l]

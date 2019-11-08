from typing import List, Union, Dict
from collections import defaultdict

# Reference : https://www.youtube.com/watch?v=CpZh4eF8QBw
def cal_z(text) -> List[int]:
    """
    Computes Z array, ie length of longest substring beginning at each index which is prefix of the string
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


def cal_prefix_arr(pat: str) -> List[int]:
    l = len(pat)
    arr = [0] * l

    j = 0
    i = 1

    while i < l:
        if pat[j] == pat[i]:
            arr[i] = j + 1
            j += 1
            i += 1
        else:
            if j == 0:
                arr[i] = 0
                i += 1
            else:
                j = arr[j - 1]

    return arr


def substring_kmp(text: str, pat: str) -> List[int]:
    i = 0
    j = 0
    n = len(text)
    m = len(pat)
    prefix = cal_prefix_arr(pat)
    idxs = []
    while i < n:
        if text[i] == pat[j]:
            i += 1
            j += 1
            if j == m:
                idxs.append(i - j)
                j = prefix[j - 1]
        else:
            if j == 0:
                i += 1
            else:
                j = prefix[j - 1]

    return idxs


def hash_cal(text: str, prime: int = 101) -> int:
    ascii_list = [ord(x) - ord("a") + 1 for x in text]
    return sum(asc * (prime ** idx) for idx, asc in enumerate(ascii_list))


def rolling_hash(prev_hash: int, pat_length: int, new_char: str, prev_char: str, prime: int = 101) -> int:
    prev_ascii = ord(prev_char) - ord("a") + 1
    new_ascii = ord(new_char) - ord("a") + 1
    new_hash = (prev_hash - prev_ascii) // prime + (new_ascii * (prime ** (pat_length - 1)))
    return new_hash


def substring_rabin_karp(text: str, pat: Union[str, List[str]], prime=101) -> Dict[str, List[int]]:
    """
    Over Engineered Rabin Karp for Multipattern matching
    """

    if isinstance(pat, str):
        pat = [pat]

    pat = list(set(pat))
    idx_dict = {p: [] for p in pat}

    text_len = len(text)
    pat_len = len(pat[0])

    if text_len < pat_len:
        return idx_dict

    if not all(len(x) == pat_len for x in pat):
        raise ValueError("Patterns of Unequal Length")

    hash_dict = defaultdict(lambda: None)
    for p in pat:
        p_hash = hash_cal(p, prime)
        if hash_dict[p_hash]:
            raise ValueError("Prime Unsuitable, Pattern Hash Collision")
        hash_dict[p_hash] = p

    running_hash = hash_cal(text[:pat_len])

    i = 0
    while True:
        p = hash_dict[running_hash]
        if p is not None and text[i : pat_len + i] == p:
            idx_dict[p].append(i)

        if i == text_len - pat_len:
            break
        running_hash = rolling_hash(running_hash, pat_len, text[i + pat_len], text[i])
        i += 1

    return idx_dict

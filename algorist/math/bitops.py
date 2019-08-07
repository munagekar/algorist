# https://codereview.stackexchange.com/a/105923
def msbit(n: int):
    last = n
    n &= n - 1
    while n != 0:
        last = n
        n &= n - 1
    return last

def extended_euclidean(a, b):
    if b == 0:
        x = 1
        y = 0
        return a, x, y
    else:
        g, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - y1 * (a // b)
        return g, x, y

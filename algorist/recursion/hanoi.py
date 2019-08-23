def _hanoi(n, from_rod, to_rod, aux_rod, movelist):
    if n == 1:
        movelist.append((n, from_rod, to_rod))
        return
    _hanoi(n - 1, from_rod, aux_rod, to_rod, movelist)
    movelist.append((n, from_rod, to_rod))
    _hanoi(n - 1, aux_rod, to_rod, from_rod, movelist)


def hanoi(n, start_tower, destination_tower, aux_tower):
    movelist = []
    _hanoi(n, start_tower, destination_tower, aux_tower, movelist)
    return movelist

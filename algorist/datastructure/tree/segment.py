class SegmentTree:
    def __init__(self, arr):
        size = 4 * len(arr)
        self.n = len(arr) - 1
        self.t = [None] * size
        self._build(arr, v=1, left=0, right=self.n)

    def update(self, diff, pos):
        self._update(v=1, diff=diff, pos=pos, sleft=0, sright=self.n)

    def _update(self, v, diff, pos, sleft, sright):
        self.t[v] += diff
        if sleft == sright:
            return
        mid = (sleft + sright) // 2
        if pos <= mid:
            self._update(v * 2, diff, pos, sleft, mid)
        else:
            self._update(v * 2 + 1, diff, pos, mid + 1, sright)

    def _build(self, arr, v, left, right):
        if left == right:
            self.t[v] = arr[left]
            return
        mid = (left + right) // 2
        self._build(arr, v * 2, left, mid)
        self._build(arr, v * 2 + 1, mid + 1, right)
        self.t[v] = self.t[v * 2] + self.t[v * 2 + 1]

    def query(self, left, right):
        return self._query(1, left, right, 0, self.n)

    def _query(self, v, left, right, sleft, sright):
        if left > right:
            return 0

        if sleft == left and sright == right:
            return self.t[v]

        mid = (sleft + sright) // 2
        left_sum = self._query(v * 2, left, min(right, mid), sleft, mid)
        right_sum = self._query(v * 2 + 1, max(left, mid + 1), right, mid + 1, sright)
        return left_sum + right_sum

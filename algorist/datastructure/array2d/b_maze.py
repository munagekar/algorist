# Module for Binary Maze
from collections import deque
from math import inf


def print2d(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = "\t".join("{{:{}}}".format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print("\n".join(table))


class BinaryMaze:
    def __init__(self, maze):
        self.maze = maze
        self.h = len(self.maze)
        self.b = len(self.maze[0])

    def shortest_path_lee(self, sx: int, sy: int, ex: int, ey: int):
        """
        Optimized Lee Algorithm Implementation
        """

        # Init
        weights = [[inf] * self.b for _ in range(self.h)]

        queue = deque()
        queue.append((sx, sy, 0))
        dist = 0
        # Wave Propogate
        while len(queue):
            cx, cy, w = queue.popleft()
            weights[cy][cx] = w
            if cx == ex and cy == ey:
                break
            if cx != 0 and weights[cy][cx - 1] == inf and self.maze[cy][cx - 1]:
                queue.insert(-1, (cx - 1, cy, w + 1))
            if cy != 0 and weights[cy - 1][cx] == inf and self.maze[cy - 1][cx]:
                queue.insert(-1, (cx, cy - 1, w + 1))
            if cx != self.b - 1 and weights[cy][cx + 1] and self.maze[cy][cx + 1]:
                queue.insert(-1, (cx + 1, cy, w + 1))
            if cy != self.h - 1 and weights[cy + 1][cx] == inf and self.maze[cy + 1][cx]:
                queue.insert(-1, (cx, cy + 1, w + 1))

        # Trace Back

        px, py, w = ex, ey, weights[ey][ex]
        result = []
        while w != 0:
            w -= 1
            print(f"at{px, py}, looking for {w}")
            if px != 0 and weights[py][px - 1] == w:
                result.append((px - 1, py))
                px -= 1
                continue

            if py != 0 and weights[py - 1][px] == w:
                result.append((px, py - 1))
                py -= 1
                continue

            if px != self.b - 1 and weights[py][px + 1] == w:
                result.append((px + 1, py))
                px += 1
                continue

            result.append((px, py + 1))
            py += 1

        return list(reversed(result)) + [(ex, ey)]

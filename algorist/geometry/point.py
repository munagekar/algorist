from enum import Enum
from math import sqrt


class Orientation(Enum):
    ANTI_CLOCKWISE = -1
    COLINEAR = 0
    CLOCKWISE = 1


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False


# Based on the slope
# Reference: https://www.geeksforgeeks.org/orientation-3-ordered-points/
def find_orientation(p1: Point, p2: Point, p3: Point) -> Orientation:
    orientation = (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)
    if orientation == 0:
        return Orientation.COLINEAR
    if orientation > 0:
        return Orientation.CLOCKWISE
    return Orientation.ANTI_CLOCKWISE


def distance(p1: Point, p2: Point = Point(0, 0)) -> float:
    diff_x = p1.x - p2.x
    diff_y = p1.y - p2.y
    return sqrt(diff_x * diff_x + diff_y * diff_y)

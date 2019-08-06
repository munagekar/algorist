from enum import Enum
from math import sqrt, atan2, pi, sin, cos, hypot


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
        return

    def __repr__(self):
        return f"Point({self.x},{self.y})"

    def __abs__(self):
        return hypot(self.x, self.y)

    def to_polar(self):
        r = abs(self)
        rad = atan2(self.y, self.x)
        return PolarPoint(r, rad)


# Based on the slope
# Reference: https://www.geeksforgeeks.org/orientation-3-ordered-points/
def find_orientation(p1: Point, p2: Point, p3: Point) -> Orientation:
    orientation = (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)
    if orientation == 0:
        return Orientation.COLINEAR
    if orientation > 0:
        return Orientation.CLOCKWISE
    return Orientation.ANTI_CLOCKWISE


def distance(p1: Point, p2: Point) -> float:
    diff_x = p1.x - p2.x
    diff_y = p1.y - p2.y
    return hypot(diff_x, diff_y)


class PolarPoint:
    def __init__(self, r: float, rad: float):
        """
        Polar Representation of a Point
        Args:
            r: magnitude ie distance from origin
            rad: angle in radians
        """
        self.r = r
        self.rad = rad % (2 * pi)

    def __eq__(self, other):
        if self.r != other.r or self.rad != other.rad:
            return False
        return True

    def __repr__(self):
        return f"PolarPoint({self.r},{self.rad})"

    def __abs__(self):
        return self.r

    def to_cartesian(self):
        x = self.r * cos(self.rad)
        y = self.r * sin(self.rad)
        return Point(x, y)

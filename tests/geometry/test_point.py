from algorist.geometry.point import Point, find_orientation, Orientation, distance, PolarPoint
from math import atan2


def test_point():
    # Equality
    a = Point(3, 4)
    assert a == a
    assert a == Point(3, 4)
    # Repr
    p = Point(1, 0)
    assert repr(p) == "Point(1,0)"
    # Abs
    assert abs(a) == 5
    # Polar Point
    angle = atan2(4, 3)
    assert Point(3, 4).to_polar() == PolarPoint(5, angle)


def test_polar_point():
    # Equality
    a = PolarPoint(3, 4)
    b = PolarPoint(3, 4)
    assert a == b
    # Repr Test
    repr(b)
    # Abs
    assert abs(a) == 3
    # tocartesian
    Point(1, 2).to_polar().to_cartesian()


def test_orientation():
    p1 = Point(0, 0)
    p2 = Point(4, 4)
    p3 = Point(1, 2)
    assert Orientation.ANTI_CLOCKWISE == find_orientation(p1, p2, p3)
    assert Orientation.CLOCKWISE == find_orientation(p1, p3, p2)
    assert Orientation.COLINEAR == find_orientation(p1, p2, Point(3, 3))


def test_distance():
    a = Point(3, 4)
    assert distance(a, a) == 0
    assert distance(a, Point(6, 8)) == 5

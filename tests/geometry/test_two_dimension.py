from random import randint

from algorist.geometry.point import Point
from algorist.geometry.two_dimension import closest_point_pair_brute, closest_point_pair


def test_closest_point_pair_brute():
    x = Point(1, 2)
    y = Point(2, 2)
    z = Point(15, 15)
    assert closest_point_pair_brute([x, y, z]) == (1, (x, y))


def test_clostest_point_pair():
    points = [Point(randint(-10e5, 10e5), randint(-10e5, 10e5)) for _ in range(1000)]
    points = list(set(points))
    d1, _ = closest_point_pair(points)
    d2, _ = closest_point_pair_brute(points)
    assert d1 == d2

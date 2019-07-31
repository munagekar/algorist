from algorist.geometry.point import Point, find_orientation, Orientation


def test_point_eq():
    a = Point(3, 4)
    assert a == a
    assert a == Point(3, 4)


def test_orientation():
    p1 = Point(0, 0)
    p2 = Point(4, 4)
    p3 = Point(1, 2)
    assert Orientation.ANTI_CLOCKWISE == find_orientation(p1, p2, p3)
    assert Orientation.CLOCKWISE == find_orientation(p1, p3, p2)
    assert Orientation.COLINEAR == find_orientation(p1, p2, Point(3, 3))

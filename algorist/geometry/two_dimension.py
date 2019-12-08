import itertools
import math
from operator import attrgetter
from typing import List

from algorist.geometry.point import Point, distance2


# Reference : Cormen
def closest_point_pair(points: List[Point]):
    # Precompute : Points Sorted by x and y coordinates
    points_x = sorted(points, key=attrgetter("x", "y"))
    points_y = sorted(points, key=attrgetter("y", "x"))

    return _closest_point_pair(points_x, points_y)


def _closest_point_pair(points_x: List[Point], points_y: List[Point]):
    l = len(points_x)
    if l <= 3:
        return closest_point_pair_brute(points_x)

    mid = l >> 1
    mid_x = points_x[mid].x

    # Compute for split
    left_x = points_x[:mid + 1]
    right_x = points_x[mid + 1:]

    left_y = []
    right_y = []
    for p in points_y:
        if p.x <= mid_x:
            left_y.append(p)
        else:
            right_y.append(p)

    # Divide
    l_dist, l_point_pair = _closest_point_pair(left_x, left_y)
    r_dist, r_point_pair = _closest_point_pair(right_x, right_y)

    # Conquer

    if l_dist < r_dist:
        dist = l_dist
        point_pair = l_point_pair

    else:
        dist = r_dist
        point_pair = r_point_pair

    # Analyze Vertical Strip
    v_strip = [p for p in points_y if abs(mid_x - p.x) <= dist]
    lvs = len(v_strip)
    for i, p in enumerate(v_strip):
        for j in range(i + 1, min(lvs, i + 8)):
            d = distance2(p, points_y[j])
            if d < dist:
                dist = d
                point_pair = v_strip[i], v_strip[j]

    return dist, point_pair


def closest_point_pair_brute(points: List[Point]):
    min_dist = math.inf
    point_pair = None
    l = len(points)
    for p1, p2 in itertools.combinations(points, 2):
        d = distance2(p1, p2)
        if d < min_dist:
            point_pair = (p1, p2)
            min_dist = d
    return min_dist, point_pair

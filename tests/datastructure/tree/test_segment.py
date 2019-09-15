from algorist.datastructure.tree.segment import SegmentTree as ST


def test_segment_tree():
    s = ST([1, 3, 5, 7, 9, 11])
    assert s.query(1, 3) == 15
    s.update(7, 1)
    assert s.query(1, 3) == 22

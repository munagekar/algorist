from algorist.datastructure.sparse_table import RSQ, RMQ


def test_rmq():
    r = RMQ([1, 2, 3, 4, 5])
    assert r.query(0, 4) == 1
    assert r.query(1, 2) == 2


def test_rsq():
    r = RSQ([1, 2, 3, 4])
    r.query(0, 2)
    r.query(0, 3)

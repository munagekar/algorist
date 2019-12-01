from algorist.datastructure.tree.treap import Treap


def test_treap():
    t = Treap.from_array([50, 30, 20, 40, 70, 60, 80])
    assert Treap.check_treap(t)
    t.delete(30)
    assert Treap.check_treap(t)
    t.delete(50)
    assert Treap.check_treap(t)

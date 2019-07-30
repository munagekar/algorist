from algorist.datastructure.unionfind.quickunion import QuickUnion as Qu


def test_qu():
    q = Qu()
    q.add_node('abcd')
    q.add_node('wxyz')
    assert q._mapping['abcd'] == 0
    assert q._mapping['wxyz'] == 1
    assert not q.connected('abcd', 'wxyz')
    q.join('abcd', 'wxyz')
    assert q.connected('abcd', 'wxyz')
    q.join('efgh', 'abcd')
    assert q.connected('abcd', 'efgh')
    assert q.connected('efgh', 'wxyz')


def test_qu_structure():
    q = Qu()
    q.join('a', 'b')
    # Try to create longer tree
    q.join('c', 'b')
    assert q._sizelist == [3, 1, 1]

    q = Qu()
    q.join('a', 'b')
    # Reverse Test case
    q.join('b', 'c')
    assert q._sizelist == [3, 1, 1]

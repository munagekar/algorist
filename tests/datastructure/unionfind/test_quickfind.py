from algorist.datastructure.unionfind import QuickFind as Qf


def test_qf():
    q = Qf()
    q.add_node("abcd")
    q.add_node("wxyz")
    assert q._mapping["abcd"] == 0
    assert q._mapping["wxyz"] == 1
    assert not q.connected("abcd", "wxyz")
    q.join("abcd", "wxyz")
    assert q.connected("abcd", "wxyz")
    q.join("efgh", "abcd")
    assert q.connected("abcd", "efgh")
    assert q.connected("efgh", "wxyz")

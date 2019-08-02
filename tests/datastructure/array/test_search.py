from algorist.datastructure.array.search import linear


def test_linear():
    arr = [1, 2, 3]
    assert linear(arr, 1) == 0
    assert linear(arr, 2) == 1
    assert linear(arr, 3) == 2

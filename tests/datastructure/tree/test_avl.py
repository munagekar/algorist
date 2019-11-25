from algorist.datastructure.tree.avl import AVLTree


def test_avl():
    a = AVLTree()
    a.insert(10)
    a.insert(20)
    a.insert(30)
    a.insert(40)
    a.insert(50)
    a.insert(25)

    assert a.root.data == 30
    assert a.root.left.data == 20
    assert a.root.right.data == 40
    assert a.root.left.left.data == 10
    assert a.root.left.right.data == 25
    assert a.root.right.right.data == 50

    a = AVLTree([9, 1, 0, -1, 5, 2, 6, 10, 11])
    a.delete(10)
    a.delete(11)
    assert a.root.data == 1
    assert a.root.left.data == 0
    assert a.root.left.left.data == -1
    assert a.root.right.data == 5
    assert a.root.right.left.data == 2
    assert a.root.right.right.data == 9
    assert a.root.right.right.left.data == 6

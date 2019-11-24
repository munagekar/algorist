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

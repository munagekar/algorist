from typing import Union
import random


class Node:
    def __init__(self, key: float):
        self.left = None
        self.right = None
        self.key = key
        self.priority = random.random()


class Treap:
    def __init__(self):
        self.root = None

    @classmethod
    def from_array(cls, arr):
        t = Treap()
        for i in arr:
            t.insert(i)
        return t

    def insert(self, key):
        self.root = self._insert(key, self.root)

    def _insert(self, key, root) -> Node:
        if root is None:
            return Node(key)

        elif root.key < key:
            root.right = self._insert(key, root.right)
            if root.priority < root.right.priority:
                return left_rotate(root)

        elif root.key > key:
            root.left = self._insert(key, root.left)
            if root.priority < root.left.priority:
                return right_rotate(root)

        # Do Nothing or raise error
        return root

    def delete(self, key: float):
        self.root = self._delete(key, self.root)

    def _delete(self, key: float, root: Node) -> Union[Node, None]:
        if root is None:
            return root

        elif root.key > key:
            root.left = self._delete(key, root.left)

        elif root.key < key:
            root.right = self._delete(key, root.right)

        else:
            # Delete Node
            if root.left is None and root.right is None:
                return None

            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            # Both left and right child exist

            if root.left.priority >= root.right.priority:
                root = right_rotate(root)
                root.right = self._delete(key, root.right)
                return root

            else:
                root = left_rotate(root)
                root.left = self._delete(key, root.left)
                return root

    @staticmethod
    def check_treap(t):
        return Treap._check_treap(t.root)

    @staticmethod
    def _check_treap(root):
        if root is None:
            return True

        if root.left is not None:
            if root.left.key < root.key and root.left.priority <= root.priority:
                if not Treap._check_treap(root.left):
                    return False
            else:
                return False

        if root.right is not None:
            if root.right.key > root.key and root.right.priority <= root.priority:
                if not Treap._check_treap(root.right):
                    return False
            else:
                return False
        return True


def left_rotate(root: Node):
    new_root = root.right
    root.right = new_root.left
    new_root.left = root
    return new_root


def right_rotate(root: Node):
    new_root = root.left
    root.left = new_root.right
    new_root.right = root
    return new_root

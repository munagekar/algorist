# References : https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
# Youtube : https://www.youtube.com/watch?v=rbg7Qf8GkQ4


from typing import Union, Optional, List


class Node:
    def __init__(self, data: float):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def right_rotate(root: Node) -> Node:
    """
    Performs a right rotation of the tree, can correct an LL imbalance in one step

    Args:
        root: The node where the operation is to be performed not necessarily the root of the tree

    Returns:
        Node : The new root post rotation.
    """
    new_root = root.left
    root.left = new_root.right
    new_root.right = root
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))
    return new_root


def left_rotate(root: Node) -> Node:
    """
    Performs a left rotation of the tree, can correct a RR imbalance in one step
    Args:
        root: The node where the operation is to be performed, doesn't mean tree root

    Returns:
        Node : The new root post rotation
    """
    new_root = root.right
    root.right = new_root.left
    new_root.left = root
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))
    return new_root


class AVLTree:
    def __init__(self, data: Optional[List[float]] = None):
        self.root = None
        if data:
            for d in data:
                self.insert(d)

    def insert(self, data: float):
        if self.root is None:
            self.root = Node(data)
            return
        self.root = self._insert(data, self.root)

    def pre_order(self):
        """
        Pre-order traversal of the tree, root,left,right order recursively

        Returns:
            None
        """
        if not self.root:
            print("Empty Tree")
        self._pre_order(self.root)

    def _pre_order(self, cur: Node, parent: Node = None, direction=None):
        """
        Pre-order Traversal printing links

        Args:
            cur: Current node being discovered
            parent: Parent of the node being discovered
            direction: Left or Right Link

        Returns:
            None
        """
        if cur is None:
            return

        if parent is None:
            print(f"Root {cur.data}")

        else:
            print(f"{direction} link from {parent.data} to {cur.data}")
        self._pre_order(cur.left, cur, "left")
        self._pre_order(cur.right, cur, "right")

    def _insert(self, key: float, root: Node) -> Node:

        if root is None:
            return Node(key)

        if key == root.data:
            raise ValueError(f"Key={key} already present")

        if key > root.data:
            root.right = self._insert(key, root.right)

        else:
            root.left = self._insert(key, root.left)

        # Up the recursion stack visiting nodes visited during traversal
        root.height = 1 + max(get_height(root.left), get_height(root.right))
        balance = get_height(root.right) - get_height(root.left)

        # RR or RL case
        if balance > 1:
            if root.right.data > key:
                root.right = right_rotate(root.right)  # Change RL to RR
            return left_rotate(root)

        # LL or LR Case
        if balance < -1:
            if root.left.data < key:
                root.left = left_rotate(root.left)  # Change LR to LL
            return right_rotate(root)

        # No balancing required
        return root

    def _delete(self, root, key) -> Union[Node, None]:
        if root is None:
            raise KeyError("Key={key} not found")
        if root.data == key:
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            root.data = get_min_value(root.right)
            root.right = self._delete(root.right, root.data)

        elif root.data > key:
            root.left = self._delete(root.left, key)
        else:
            root.right = self._delete(root.right, key)

        # Up the recursion stack visiting nodes already visited during traversal
        root.height = 1 + max(get_height(root.left), get_height(root.right))
        balance = get_height(root.right) - get_height(root.left)

        # RR or RL
        if balance > 1:
            if get_height(root.right.right) - get_height(root.right.left) < 0:  # Change RL to RR
                root.right = right_rotate(root.right)
            return left_rotate(root)

        # LL or LR case
        if balance < -1:
            if get_height(root.left.right) - get_height(root.left.left) > 0:  # Change LR to LL
                root.left = left_rotate(root.left)
            return right_rotate(root)

        # No balancing required
        return root

    def delete(self, key: float):
        if self.root is None:
            raise KeyError(f"Empty Tree has no key={key}")
        self.root = self._delete(self.root, key)


def get_height(node: Union[None, Node]) -> int:
    return 0 if not node else node.height


def get_min_value(node) -> int:
    if node.left is None:
        return node.data
    return get_min_value(node.left)

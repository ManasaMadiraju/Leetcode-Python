class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, root):
        if root:
            self._print_tree(root.left)
            print(root.val, end=' ')
            self._print_tree(root.right)

if __name__ == "__main__":
    tree = BinaryTree()
    elements = [10, 5, 20, 3, 7, 15, 30]

    for elem in elements:
        tree.insert(elem)

    tree.print_tree()

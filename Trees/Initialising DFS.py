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

    def dfs_in_order(self):
        self._dfs_in_order(self.root)

    def _dfs_in_order(self, root):
        if root:
            self._dfs_in_order(root.left)
            print(root.val, end=' ')
            self._dfs_in_order(root.right)

    def dfs_pre_order(self):
        self._dfs_pre_order(self.root)

    def _dfs_pre_order(self, root):
        if root:
            print(root.val, end=' ')
            self._dfs_pre_order(root.left)
            self._dfs_pre_order(root.right)

    def dfs_post_order(self):
        self._dfs_post_order(self.root)

    def _dfs_post_order(self, root):
        if root:
            self._dfs_post_order(root.left)
            self._dfs_post_order(root.right)
            print(root.val, end=' ')


if __name__ == "__main__":
    tree = BinaryTree()
    elements = [10, 5, 20, 3, 7, 15, 30]

    for elem in elements:
        tree.insert(elem)

    print("In-order DFS traversal:")
    tree.dfs_in_order()
    print()

    print("Pre-order DFS traversal:")
    tree.dfs_pre_order()
    print()

    print("Post-order DFS traversal:")
    tree.dfs_post_order()
    print()


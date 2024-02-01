class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _update_height(self, node):
        if not node:
            return 0
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, z):
        y = z.left
        T2 = y.right

        y.right = z
        z.left = T2

        self._update_height(z)
        self._update_height(y)

        return y

    def _rotate_left(self, y):
        x = y.right
        T2 = x.left

        x.left = y
        y.right = T2

        self._update_height(y)
        self._update_height(x)

        return x

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return TreeNode(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        else:
            return root  # Duplicate keys are not allowed

        self._update_height(root)

        balance = self._balance_factor(root)

        # Left-Left Case
        if balance > 1 and key < root.left.key:
            return self._rotate_right(root)

        # Right-Right Case
        if balance < -1 and key > root.right.key:
            return self._rotate_left(root)

        # Left-Right Case
        if balance > 1 and key > root.left.key:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        # Right-Left Case
        if balance < -1 and key < root.right.key:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        if not root:
            return root

        self._update_height(root)

        balance = self._balance_factor(root)

        # Left-Left Case
        if balance > 1 and self._balance_factor(root.left) >= 0:
            return self._rotate_right(root)

        # Left-Right Case
        if balance > 1 and self._balance_factor(root.left) < 0:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        # Right-Right Case
        if balance < -1 and self._balance_factor(root.right) <= 0:
            return self._rotate_left(root)

        # Right-Left Case
        if balance < -1 and self._balance_factor(root.right) > 0:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.key)
            self._inorder_traversal(root.right, result)

# Example Usage:
vector = [70,50,30,10,20,40,60]
avl_tree = AVLTree()
for i in vector:
    avl_tree.insert(i)

print("Unorder Vector:", vector ) 
print("Inorder Traversal:", avl_tree.inorder_traversal())

# Output: Inorder Traversal: [20, 30, 40, 50, 60, 70, 80]
avl_tree.delete(30)
print("Inorder Traversal after deletion:", avl_tree.inorder_traversal())
# Output: Inorder Traversal after deletion: [20, 40, 50, 60, 70, 80]

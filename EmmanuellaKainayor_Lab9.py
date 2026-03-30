# Task: Given a BST, write three functions
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Insert a value into the BST
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


# Number of edges from the root to the deepest leaf.
def height(node):
    if node is None:
        return -1
    left_h = height(node.left)
    right_h = height(node.right)
    return 1 + max(left_h, right_h)


# Keep going left until there is no left child.
def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.value


# Keep going right until there is no right child.
def find_max(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.value


# Build the BST
values = [10, 5, 15, 2, 7, 20]
root = None
for v in values:
    root = insert(root, v)

print("Height:", height(root))
print("Min:", find_min(root))
print("Max:", find_max(root))

# Insert one more value
root = insert(root, 8)

print("Height:", height(root))
print("Min:", find_min(root))
print("Max:", find_max(root))

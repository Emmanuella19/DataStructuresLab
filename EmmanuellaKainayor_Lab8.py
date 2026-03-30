# Task: Given the root node of a parse tree representing a mathematical expression, write a Python function named evaluate(node) that computes and returns the result of that expression.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Construct the parse tree for ((7 + 3) * (5 - 2))
root = Node('*')
root.left = Node('+')
root.right = Node('-')
root.left.left = Node(7)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(2)

# Function to evaluate the parse tree
def evaluate(node):
    if node.left is None and node.right is None:
        return node.value

    # Recursively evaluate the left and right subtrees
    left_value = evaluate(node.left)
    right_value = evaluate(node.right)

    if node.value == '+':
        return left_value + right_value

    if node.value == "-":
        return left_value - right_value

    if node.value == "*":
        return left_value * right_value

    if node.value == "/":
        return left_value / right_value


print(evaluate(root)) # Should print 30.0
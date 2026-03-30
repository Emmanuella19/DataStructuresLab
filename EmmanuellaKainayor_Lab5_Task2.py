# Write a method named findLength(doublyNode) that takes any node of a doubly linked list as input and returns the length of the list.
# Can you determine the length without visiting any node more than once?

def findLength(doublyNode):
    count = 1   # count the starting node

    # Walk backward to the head
    current = doublyNode.prev
    while current is not None:
        count += 1
        current = current.prev

    # Walk forward to the tail
    current = doublyNode.next
    while current is not None:
        count += 1
        current = current.next

    return count


# -------------------------
# DOUBLY LINKED LIST NODE
# -------------------------

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# -------------------------
# HELPER: PRINT LIST
# -------------------------

def print_doubly_list(head):
    current = head
    while current is not None:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")


# -------------------------
# DRIVER CODE / EXAMPLE USAGE
# -------------------------

# Create nodes
n1 = DoublyNode(10)
n2 = DoublyNode(20)
n3 = DoublyNode(30)
n4 = DoublyNode(40)

# Link them: 10 <-> 20 <-> 30 <-> 40
n1.next = n2

n2.prev = n1
n2.next = n3

n3.prev = n2
n3.next = n4

n4.prev = n3

# Print the list
print("Doubly Linked List:")
print_doubly_list(n1)

# Test findLength from different starting points
print("\nLength starting from node 10:", findLength(n1))
print("Length starting from node 20:", findLength(n2))
print("Length starting from node 30:", findLength(n3))
print("Length starting from node 40:", findLength(n4))

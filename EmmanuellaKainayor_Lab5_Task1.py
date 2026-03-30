def length(head):
    # Count how many nodes are in the linked list
    count = 0
    current = head

    # Traverse the list until we reach the end
    while current is not None:
        count += 1
        current = current.next

    return count


def get_tail(head):
    # If the list is empty, there is no tail
    if head is None:
        return None

    # Start at the head and move forward until the last node
    current = head
    while current.next is not None:
        current = current.next

    # 'current' now refers to the last node in the list
    return current


def concatenate(h1, h2):
    # Compute the lengths of both linked lists
    len1 = length(h1)
    len2 = length(h2)

    # Determine which list should come first based on length
    if len1 < len2:
        first = h1
        second = h2
    else:
        first = h2
        second = h1

    # If the first list is empty, the result is just the second list
    if first is None:
        return second

    # Find the last node of the first list
    tail = get_tail(first)

    # Attach the second list to the end of the first
    tail.next = second

    # Return the head of the combined list
    return first


# Simple Node class for testing
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Helper to print a linked list
def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# -------------------------
# DRIVER CODE / EXAMPLE USAGE
# -------------------------

# Create first list: 3 -> 4 -> 5
h1 = Node(3)
h1.next = Node(4)
h1.next.next = Node(5)

# Create second list: 10 -> 20
h2 = Node(10)
h2.next = Node(20)

print("List 1:")
print_list(h1)

print("List 2:")
print_list(h2)

# Concatenate based on length
result = concatenate(h1, h2)

print("Concatenated result:")
print_list(result)

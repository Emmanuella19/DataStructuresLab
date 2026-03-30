class Node:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.count += 1
            return

        self.tail.next = new_node
        self.tail = new_node
        self.count += 1

    def dequeue(self):
        if self.head is None:
            return None

        removed_value = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.count -= 1
        return removed_value

    def front(self):
        if self.head is None:
            return None
        return self.head.value

    def size(self):
        return self.count



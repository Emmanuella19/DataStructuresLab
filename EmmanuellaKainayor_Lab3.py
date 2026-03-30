class TwoStacks:

    def __init__(self, n):
        self.data = [None] * n
        self.left_top = -1
        self.right_top = n
        self.capacity = n

    def push_left(self, item):
        if self.left_top + 1 == self.right_top:
            print("Stack Overflow (left)")
            return
        self.left_top += 1
        self.data[self.left_top] = item

    def push_right(self, item):
        if self.left_top + 1 == self.right_top:
            print("Stack Overflow (right)")
            return
        self.right_top -= 1
        self.data[self.right_top] = item

    def pop_left(self):
        if self.left_top == -1:
            return None
        top_item = self.data[self.left_top]
        self.left_top -= 1
        return top_item

    def pop_right(self):
        if self.right_top == self.capacity:
            return None
        top_item = self.data[self.right_top]
        self.right_top += 1
        return top_item

    def len_left(self):
        return self.left_top + 1

    def len_right(self):
        return self.capacity - self.right_top

    def transfer_to_left(self, n):
        for _ in range(n):
            item = self.pop_right()
            if item is None:
                print("Not enough items in right stack")
                return
            self.push_left(item)

    def transfer_to_right(self, n):
        for _ in range(n):
            item = self.pop_left()
            if item is None:
                print("Not enough items in left stack")
                return
            self.push_right(item)


def main():
    ts = TwoStacks(6)

    print("Initial state:", ts.data)

    ts.push_left(1)
    ts.push_left(2)
    print("After pushing left:", ts.data)

    ts.push_right(9)
    ts.push_right(8)
    print("After pushing right:", ts.data)

    print("Pop left:", ts.pop_left())
    print("After pop left:", ts.data)

    print("Pop right:", ts.pop_right())
    print("After pop right:", ts.data)

    ts.push_right(7)
    ts.push_right(6)
    print("Before transfer:", ts.data)

    ts.transfer_to_left(2)
    print("After transferring 2 items to left:", ts.data)

    print("Left length:", ts.len_left())
    print("Right length:", ts.len_right())


if __name__ == "__main__":
    main()

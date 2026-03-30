class MyCustomMap:
    def __init__(self, N):
        self.size = N
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hash(self, key):
        if isinstance(key, int):
            return key

        elif isinstance(key, float):
            float_str = str(key)
            parts = float_str.split('.')
            new_float = parts[1]
            newer_float = int(new_float)
            return newer_float

        elif isinstance(key, str):
            hash = 0
            base = 31
            for char in key:
                hash = hash * base + ord(char)
            return hash

        else:
            raise Exception("The given key is not supported!")

    # Modified put() using double hashing
    def put(self, key, value):
        hash_code = self.hash(key)

        h1 = hash_code % 13
        h2 = 1 + (hash_code % 11)

        for i in range(self.size):
            index = (h1 + i * h2) % self.size

            if self.keys[index] is None:
                self.keys[index] = key
                self.values[index] = value
                return

            if self.keys[index] == key:
                self.values[index] = value
                return

        raise Exception("HashMap is full! No available slot for insertion.")

# driver code
if __name__ == "__main__":
    my_map = MyCustomMap(20)

    my_map.put("apple", 1)
    my_map.put("banana", 2)
    my_map.put("orange", 3)

    print(my_map.get("apple"))   # Output: 1
    print(my_map.get("banana"))  # Output: 2
    print(my_map.get("orange"))  # Output: 3
    print(my_map.get("grape"))   # Output: None (key not found)
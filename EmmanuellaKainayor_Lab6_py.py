class MyCustomMap:
    def __init__(self, N):
        self.size = N
        self.keys = [None] * self.size  # Stores keys
        self.values = [None] * self.size  # Stores corresponding values

    def hash(self, key):
        if isinstance(key, int): # if the key is an integer, return the key itself as the hash value
            return key

        elif isinstance(key, float):
            # if the key is a float, convert it to a string, split it at the decimal point,
            # and return the part after the decimal point as an integer
            float_str = str(key)
            parts = float_str.split('.')
            new_float = parts[1]
            newer_float = int(new_float)
            return newer_float

        elif isinstance(key, str):
            # if the key is a string, calculate the hash value by iterating through each character in the string,
            # multiplying the current hash value by a base (31 in this case) and adding the ASCII value of the character
            hash = 0 # initialize hash value to 0
            base = 31 # a common choice for the base in string hashing
            for char in key: # iterate through each character in the string
                hash = hash * base + ord(char) # update the hash value by multiplying the current hash value by the base and adding the ASCII value of the character
            return hash

        else: # if the key is of an unsupported type, raise an exception
            raise Exception("The given key is not supported!")

    def put(self, key, value):
        hash_code = self.hash(key) # calculate the hash code for the given key
        index = hash_code % self.size

        if self.keys[index] is not None:
            raise Exception("Collision occurred!")
        self.keys[index] = key # store the key at the calculated index
        self.values[index] = value # store the corresponding value at the same index

    def get(self, key):
        hash_code = self.hash(key) # calculate the hash code for the given key
        index = hash_code % self.size

        if self.keys[index] is None: # if there is no key at the calculated index, return None
            return None
        if self.keys[index] == key: # if the key at the calculated index matches the given key, return the corresponding value
            return self.values[index]

        return None

    def __setitem__(self, key, value):
        self.put(key, value) # call the put method to store the key-value pair

    def __getitem(self, key):
        return self.get(key) # call the get method to retrieve the value associated with the given key








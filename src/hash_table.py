class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def get_size(self):
        return self.size

    def _hash_function(self, key):
        hv = 0
        for char in key:
            hv += ord(char)
        return hv % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        print(self.table[index])
        x = self.table[index][0][1]
        return x

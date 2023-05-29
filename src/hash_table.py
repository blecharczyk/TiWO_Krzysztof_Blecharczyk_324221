class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def get_size(self):
        return self.size

    def _hash_function(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def insert(self, key, value):
        self.table[self._hash_function(key)].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        print(self.table[index])
        return self.table[index][0][1]

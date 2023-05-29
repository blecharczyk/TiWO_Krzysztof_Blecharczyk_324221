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
        for entry in self.table[self._hash_function(key)]:
            if entry[0] == key:
                entry[1] = value

        self.table[self._hash_function(key)].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        for entry in self.table[index]:
            if entry[0] == key:
                return entry[1]

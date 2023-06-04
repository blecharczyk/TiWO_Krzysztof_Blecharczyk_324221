from src.helpers.terminal_colors import TerminalColors


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
        index = self._hash_function(key)
        for entry in self.table[index]:
            if entry[0] == key:
                entry[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        for entry in self.table[index]:
            if entry[0] == key:
                return entry[1]
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key):
        index = self._hash_function(key)
        for i, entry in enumerate(self.table[index]):
            if entry[0] == key:
                del self.table[index][i]
                return
        raise KeyError(f"Key '{key}' not found")

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

    def print_hash_table(self):
        for index, bucket in enumerate(self.table):
            print(f"Index {index}:")
            for entry in bucket:
                print(f"  Key: {entry[0]}, Value: {entry[1]}")
            print()

    def print_hash_table_with_color(self, key):
        for index, bucket in enumerate(self.table):
            print(f"Index {index}:")
            for entry in bucket:
                if entry[0] == key:
                    print(
                        f"  Key: {TerminalColors.OKGREEN + entry[0] + TerminalColors.ENDC}, Value: {TerminalColors.RED + entry[1] + TerminalColors.ENDC}"
                    )
                else:
                    print(f"  Key: {entry[0]}, Value: {entry[1]}")
            print()

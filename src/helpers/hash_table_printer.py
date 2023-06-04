from src.helpers.terminal_colors import TerminalColors


class HashTablePrinter:
    def __init__(self):
        pass

    def print_hash_table(self, hash_table):
        for index, bucket in enumerate(hash_table.table):
            print(f"Index {index}:")
            for entry in bucket:
                print(f"  Key: {entry[0]}, Value: {entry[1]}")
            print()

    def print_hash_table_with_color(self, hash_table, key):
        for index, bucket in enumerate(hash_table.table):
            print(f"Index {index}:")
            for entry in bucket:
                if entry[0] == key:
                    print(
                        f"  Key: {TerminalColors.OKGREEN + entry[0] + TerminalColors.ENDC}, Value: {TerminalColors.RED + entry[1] + TerminalColors.ENDC}"
                    )
                else:
                    print(f"  Key: {entry[0]}, Value: {entry[1]}")
            print()

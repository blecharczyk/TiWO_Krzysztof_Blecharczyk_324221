from hash_table import HashTable

class TextGui:
    def __init__(self):
        pass

    def display_menu(self):
        print(
            "There are 3 options to choose from:\n"
            "1. display a predefined example showing how the hash table works\n"
            "2. display an advanced example showing how the hash table works\n"
            "3. quit the application\n"
        )

    def process_choice(self, choice):
        if choice == "1":
            print("Option 1 - predefined example")
            self.show_predefined_example()
        elif choice == "2":
            print("Option 2")
        elif choice == "3":
            print("Option 3. Exit .")
            return False
        else:
            print("Wrong choice - please try once again")

        return True

    def show_predefined_example(self):
        hash_table = HashTable(10)
        hash_table.insert("key1", "value1")
        hash_table.insert("key2", "value2")
        hash_table.insert("key3", "value3")
        hash_table.insert("key4", "value4")
        hash_table.insert("key5", "value5")
        hash_table.insert("key6", "value6")
        hash_table.insert("key7", "value3")
        hash_table.insert("key8", "value4")
        hash_table.insert("key9", "value5")
        hash_table.insert("key10", "value6")
        hash_table.insert("key11", "value6")
        hash_table.print_hash_table()
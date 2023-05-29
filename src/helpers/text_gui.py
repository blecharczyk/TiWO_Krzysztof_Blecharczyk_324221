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
            print("Option 1")
        elif choice == "2":
            print("Option 2")
        elif choice == "3":
            print("Option 3. Exit .")
            return False
        else:
            print("Wrong choice - please try once again")

        return True

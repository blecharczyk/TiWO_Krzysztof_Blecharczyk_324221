from helpers.terminal_colors import TerminalColors
from helpers.predefined_example import PredefinedExample


class TextGui:
    def __init__(self):
        pass

    def display_menu(self):
        print(
            TerminalColors.OKCYAN
            + "There are 3 options to choose from:\n"
            + TerminalColors.RED
            + "1. display a predefined example showing how the hash table works\n"
            + TerminalColors.OKGREEN
            + "2. display an advanced example showing how the hash table works\n"
            + TerminalColors.WARNING
            + "3. quit the application\n"
            + TerminalColors.ENDC
        )

    def process_choice(self, choice):
        if choice == "1":
            print("Option 1 - predefined example")
            predefined_example = PredefinedExample()
            predefined_example.show_predefined_example()
        elif choice == "2":
            print("Option 2")
        elif choice == "3":
            print("Option 3. Exit .")
            return False
        else:
            print("Wrong choice - please try once again")

        return True

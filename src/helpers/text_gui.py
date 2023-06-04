from src.helpers.terminal_colors import TerminalColors
from src.helpers.predefined_example import PredefinedExample
from src.helpers.advanced_example import AdvancedExample
from src.helpers.run_tests import RunTests
import os


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


class TextGui:
    def __init__(self):
        pass

    def display_menu(self):
        print(
            "There are 3 options to choose from:\n"
            + TerminalColors.RED
            + "1. display a predefined example showing how the hash table works\n"
            + TerminalColors.OKGREEN
            + "2. display an advanced example showing how the hash table works\n"
            + TerminalColors.WARNING
            + "3. run tests and see the output\n"
            + TerminalColors.OKCYAN
            + "4. quit the application\n"
            + TerminalColors.ENDC
        )

    def process_choice(self, choice):
        if choice == "1":
            print("Option 1 - predefined example\n")
            predefined_example = PredefinedExample()
            predefined_example.show_predefined_example()
        elif choice == "2":
            print("Option 2")
            clear_terminal()
            advanced_example = AdvancedExample()
            advanced_example.show_advanced_example()
        elif choice == "3":
            print("Option 3 - running tests\n")
            run_tests = RunTests()
            run_tests.run_tests()
        elif choice == "4":
            print("Option 4. Exit .")
            return False
        else:
            print("Wrong choice - please try once again")

        return True

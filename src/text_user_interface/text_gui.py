from src.helpers.terminal_colors import TerminalColors
from src.text_user_interface.examples.predefined_example import PredefinedExample
from src.text_user_interface.examples.advanced_example import AdvancedExample
from src.text_user_interface.run_tests import RunTests
from src.helpers.utils import clear_terminal


class TextGui:
    def __init__(self):
        pass

    def display_menu(self):
        print(
            "There are 4 options to choose from:\n"
            + TerminalColors.RED
            + "1. View a predefined example of how the hash table works\n"
            + TerminalColors.OKGREEN
            + "2. Run an advanced example of how the hash table works\n"
            + TerminalColors.WARNING
            + "3. Run tests and check the results\n"
            + TerminalColors.OKCYAN
            + "4. Quit the app\n"
            + TerminalColors.ENDC
        )

    def process_choice(self, choice):
        if choice == "1":
            predefined_example = PredefinedExample()
            predefined_example.show_predefined_example()
        elif choice == "2":
            clear_terminal()
            advanced_example = AdvancedExample()
            advanced_example.show_advanced_example()
        elif choice == "3":
            run_tests = RunTests()
            run_tests.run_tests()
        elif choice == "4":
            print("Option 4. Exit")
            return False
        else:
            print(
                TerminalColors.RED
                + "Wrong choice - please try once again"
                + TerminalColors.ENDC
            )

        return True

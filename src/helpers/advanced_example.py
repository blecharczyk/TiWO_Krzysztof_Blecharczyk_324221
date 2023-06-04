import os
import time
from src.hash_table import HashTable
from src.helpers.terminal_colors import TerminalColors


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


class AdvancedExample:
    def __init__(self):
        number = self.get_hash_table_size()
        self.hash_table = HashTable(number)
        self.step_number = 1

    def get_hash_table_size(self):
        while True:
            try:
                number = int(
                    input(
                        TerminalColors.OKCYAN
                        + "Insert hash_table size: "
                        + TerminalColors.ENDC
                    )
                )
                if number > 0:
                    return number
                else:
                    print(
                        TerminalColors.RED
                        + "Value can not be zero"
                        + TerminalColors.ENDC
                    )
            except ValueError:
                print("Wrong number format. Try again.")

    def insert_element_and_print_step(self):
        key = input(TerminalColors.OKGREEN + "enter key: " + TerminalColors.ENDC)
        value = input(TerminalColors.RED + "enter value: " + TerminalColors.ENDC)
        clear_terminal()
        print(
            f"Step {self.step_number} - Insert or update element: {TerminalColors.OKGREEN + key + TerminalColors.ENDC}, {TerminalColors.RED + value + TerminalColors.ENDC}\n\n *** \n"
        )
        self.step_number += 1
        time.sleep(1)
        self.hash_table.insert(key, value)
        self.hash_table.print_hash_table_with_color(key)

        time.sleep(3)
        clear_terminal()

    def remove_element_and_print_step(self):
        clear_terminal()
        key = input(
            TerminalColors.OKGREEN + "enter key to remove: " + TerminalColors.ENDC
        )
        print(
            f"Step {self.step_number} - Removing {TerminalColors.OKGREEN + key + TerminalColors.ENDC} element\n\n *** \n"
        )
        self.step_number += 1
        time.sleep(1)
        try:
            self.hash_table.remove(key)
        except KeyError:
            print(
                TerminalColors.RED
                + "Can not remove nonexisting element"
                + TerminalColors.ENDC
            )
            time.sleep(3)
            clear_terminal()
            return
        self.hash_table.print_hash_table()

        time.sleep(3)
        clear_terminal()

    def show_advanced_example_menu(self):
        print(
            "Advanced Example Menu:\n"
            + TerminalColors.RED
            + "1. Add element to hash table\n"
            + TerminalColors.OKGREEN
            + "2. Remove element from hash table\n"
            + TerminalColors.WARNING
            + "3. Exit Advanced Example menu\n"
            + TerminalColors.ENDC
        )

        print("\n**** Hash Table ****\n")
        self.hash_table.print_hash_table()
        print("****")

    def show_advanced_example(self):
        clear_terminal()

        while True:
            self.show_advanced_example_menu()
            wybor = input("Wybierz opcję: ")
            if wybor == "1":
                self.insert_element_and_print_step()
            elif wybor == "2":
                self.remove_element_and_print_step()
            elif wybor == "3":
                break
            else:
                print(
                    TerminalColors.RED
                    + "Wrong value, please try again"
                    + TerminalColors.ENDC
                )

        clear_terminal()
        print(
            TerminalColors.OKCYAN
            + "This was a presentation of a advanced example"
            + TerminalColors.ENDC
        )

        time.sleep(3)
        clear_terminal()

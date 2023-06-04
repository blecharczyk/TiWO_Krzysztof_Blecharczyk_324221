import time
from src.hash_table import HashTable
from src.helpers.terminal_colors import TerminalColors
from src.helpers.utils import clear_terminal
from src.helpers.hash_table_printer import HashTablePrinter


class PredefinedExample:
    def __init__(self):
        self.hash_table = HashTable(4)
        self.step_number = 1
        self.hash_table_printer = HashTablePrinter()

    def insert_element_and_print_step(self, key, value):
        print(
            f"Step {self.step_number} - insert {TerminalColors.OKGREEN + key + TerminalColors.ENDC}, {TerminalColors.RED + value + TerminalColors.ENDC} element\n\n *** \n"
        )
        self.step_number += 1
        time.sleep(1)
        self.hash_table.insert(key, value)
        self.hash_table_printer.print_hash_table_with_color(self.hash_table, key)

        time.sleep(3)
        clear_terminal()

    def update_element_and_print_step(self, key, value):
        print(
            f"Step {self.step_number} - update {TerminalColors.OKGREEN + key + TerminalColors.ENDC} value from {TerminalColors.RED + self.hash_table.get(key) + TerminalColors.ENDC} to {TerminalColors.RED + value + TerminalColors.ENDC} \n\n *** \n"
        )
        self.step_number += 1
        time.sleep(1)
        self.hash_table.insert(key, value)
        self.hash_table_printer.print_hash_table_with_color(self.hash_table, key)

        time.sleep(3)
        clear_terminal()

    def remove_element_and_print_step(self, key):
        print(
            f"Step {self.step_number} - remove {TerminalColors.OKGREEN + key + TerminalColors.ENDC} element\n\n *** \n"
        )
        self.step_number += 1
        time.sleep(1)
        self.hash_table.remove(key)
        self.hash_table_printer.print_hash_table(self.hash_table)

        time.sleep(3)
        clear_terminal()

    def show_predefined_example(self):
        clear_terminal()

        print(f"Step {self.step_number} - Hash Table is empty\n\n *** \n")
        self.step_number += 1
        self.hash_table_printer.print_hash_table(self.hash_table)

        time.sleep(3)
        clear_terminal()

        self.insert_element_and_print_step("dog", "hau hau")
        self.insert_element_and_print_step("cat", "miau miau")
        self.insert_element_and_print_step("chicken", "ko ko")
        self.insert_element_and_print_step("cow", "muu muu")
        self.insert_element_and_print_step("horse", "ihaha ihaha")

        self.update_element_and_print_step("chicken", "kukuryku")
        self.update_element_and_print_step("dog", "wof wof")

        self.remove_element_and_print_step("chicken")
        self.remove_element_and_print_step("cow")
        self.remove_element_and_print_step("cat")
        self.remove_element_and_print_step("horse")
        self.remove_element_and_print_step("dog")

        print(
            TerminalColors.OKCYAN
            + "This was a presentation of a predefined example"
            + TerminalColors.ENDC
        )

        time.sleep(3)
        clear_terminal()

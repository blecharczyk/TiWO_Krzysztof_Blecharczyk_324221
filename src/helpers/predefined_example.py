import os
import time
from hash_table import HashTable
from helpers.terminal_colors import TerminalColors


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


class PredefinedExample:
    def __init__(self):
        pass

    def insert_element_and_print_step(self, step_number, key, value, hash_table):
        print(
            f"Step {step_number} - Insert {TerminalColors.OKGREEN + key + TerminalColors.ENDC}, {TerminalColors.RED + value + TerminalColors.ENDC} element\n\n *** \n"
        )
        time.sleep(1)
        hash_table.insert(key, value)
        hash_table.print_hash_table_with_color(key)

        time.sleep(3)
        clear_terminal()

    def update_element_and_print_step(self, step_number, key, value, hash_table):
        print(
            f"Step {step_number} - Update {TerminalColors.OKGREEN + key + TerminalColors.ENDC} value from {TerminalColors.RED + hash_table.get(key) + TerminalColors.ENDC} to {TerminalColors.RED + value + TerminalColors.ENDC} \n\n *** \n"
        )
        time.sleep(1)
        hash_table.insert(key, value)
        hash_table.print_hash_table_with_color(key)

        time.sleep(3)
        clear_terminal()

    def remove_element_and_print_step(self, step_number, key, hash_table):
        print(
            f"Step {step_number} - Removing {TerminalColors.OKGREEN + key + TerminalColors.ENDC} element\n\n *** \n"
        )
        time.sleep(1)
        hash_table.remove(key)
        hash_table.print_hash_table()

        time.sleep(3)
        clear_terminal()

    def show_predefined_example(self):
        clear_terminal()

        print("Step 1 - Hash Table is empty\n\n *** \n")
        hash_table = HashTable(4)
        hash_table.print_hash_table()

        time.sleep(3)
        clear_terminal()

        self.insert_element_and_print_step(2, "dog", "hau hau", hash_table)
        self.insert_element_and_print_step(3, "cat", "miau miau", hash_table)
        self.insert_element_and_print_step(4, "chicken", "ko ko", hash_table)
        self.insert_element_and_print_step(5, "cow", "muu muu", hash_table)
        self.insert_element_and_print_step(6, "horse", "ihaha ihaha", hash_table)

        self.update_element_and_print_step(7, "chicken", "kukuryku", hash_table)
        self.update_element_and_print_step(8, "dog", "wof wof", hash_table)

        self.remove_element_and_print_step(9, "chicken", hash_table)
        self.remove_element_and_print_step(10, "cow", hash_table)
        self.remove_element_and_print_step(11, "cat", hash_table)
        self.remove_element_and_print_step(12, "horse", hash_table)
        self.remove_element_and_print_step(13, "dog", hash_table)

        print("This was a presentation of a predefined example")

        time.sleep(3)
        clear_terminal()

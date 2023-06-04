from src.helpers.text_gui import TextGui


def main():
    gui = TextGui()

    running = True

    while running:
        gui.display_menu()
        choice = input("Wybierz opcję: ")
        running = gui.process_choice(choice)


if __name__ == "__main__":
    main()

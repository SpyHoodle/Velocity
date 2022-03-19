from core.colors import Codes as c
import traceback
import curses
import sys


def clear(instance, y: int, x: int):
    # Clear the line at the screen at position y, x
    instance.screen.insstr(y, x, " " * (instance.width - x))


def welcome(screen):
    # Get window height and width
    height, width = screen.getmaxyx()

    # Startup text
    title = "λ Lambda"
    subtext = [
        "Next generation hackable text editor for nerds",
        "",
        "Type :h to open the README.md document",
        "Type :o <file> to open a file and edit",
        "Type :q or <C-c> to quit lambda.py"
    ]

    # Centering calculations
    start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
    start_y = int((height // 2) - 2)

    # Rendering title
    screen.addstr(start_y, start_x_title, title, curses.color_pair(7) | curses.A_BOLD)

    # Print the subtext
    for text in subtext:
        start_y += 1
        start_x = int((width // 2) - (len(text) // 2) - len(text) % 2)
        screen.addstr(start_y, start_x, text)


def prompt(instance, message: str, color: int = 1) -> (list, None):
    # Initialise the input list
    inp = []

    # Write the message to the screen
    instance.screen.addstr(instance.height - 1, 0, message, curses.color_pair(color))

    while True:
        # Wait for a keypress
        key = instance.screen.getch()

        # Subtracting a key (backspace)
        if key in (curses.KEY_BACKSPACE, 127, '\b'):
            # Write whitespace over characters to refresh it
            clear(instance, instance.height - 1, 0)

            if inp:
                # Subtract a character from the input list
                inp.pop()

            else:
                # Exit the prompt without returning the input
                return None

        elif key == 27:
            # Exit the prompt, without returning the input
            return None

        elif key in (curses.KEY_ENTER, ord('\n'), ord('\r'), ord(":"), ord(";")):
            # Return the input list
            return inp

        else:
            # If any other key is typed, append it
            # As long as the key is in the valid list
            valid = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ!"
            if chr(key) in valid and len(inp) < (instance.width - 2):
                inp.append(chr(key))

        # Write the message to the screen
        instance.screen.addstr(instance.height - 1, 0, message, curses.color_pair(color))

        # Join the input together for visibility on the screen
        input_text = "".join(inp)

        # Write the input text to the screen
        instance.screen.addstr(instance.height - 1, len(message), input_text)


def goodbye(instance):
    choice = prompt(instance, "Really quit lambda? (y/n): ", 11)
    if choice and choice[0] == "y":
        curses.endwin()
        sys.exit()

    else:
        clear(instance, instance.height - 1, 0)


def error(instance, message: str):
    # Parse the error message
    error_message = f"ERROR: {message}"

    # Write the entire message to the screen
    instance.screen.addstr(instance.height - 1, 0, f"ERROR: {message}", curses.color_pair(3))
    instance.screen.addstr(instance.height - 1, len(error_message) + 1, f"(press any key)")

    # Wait for a keypress
    instance.screen.getch()

    # Clear the bottom of the screen
    clear(instance, instance.height - 1, 0)


def fatal_error(exception: Exception):
    # Clean up the screen
    curses.endwin()

    # Print the error message and traceback
    print(f"{c.red}FATAL ERROR:{c.end} "
          f"{c.yellow}{exception}{c.end}\n")
    print(traceback.format_exc())

    # Exit, with an error exit code
    sys.exit(0)

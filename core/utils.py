import curses
import json
import os
import sys
import traceback
from pathlib import Path

from core.colors import Codes as Col
from core import cursors


def gracefully_exit():
    # Close the curses window
    curses.endwin()

    # Finally, exit the program
    sys.exit()


def clear(instance, y: int, x: int):
    # Clear the line at the screen at position y, x
    instance.screen.insstr(y, x, " " * (instance.width - x))


def pause(message: str):
    # End the curses session
    curses.endwin()

    # Print the message and wait for enter key
    input(f"{message}\n\n Press enter to continue...")


def load_file(file_path: str) -> dict:
    # load the json file with read permissions
    with open(file_path, "r") as f:
        return json.load(f)


def save_file(instance, file_path: str, data: list):
    # Save the data to the file
    with open(file_path, "w") as f:
        try:
            for index, line in enumerate(data):
                if index == len(data) - 1:
                    f.write(line)
                else:
                    f.write(f"{line}\n")

        except Exception:
            error(instance, f"File {file_path} could not be saved.")


def load_config() -> dict:
    # Parse the path of the config file
    config_file_path = f"{Path.home()}/.config/lambda/config.json"

    # Only if the config file exists, attempt to load it
    if os.path.exists(config_file_path):
        # Return the loaded config
        return load_file(config_file_path)


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

    # Write whitespace over characters to refresh it
    clear(instance, instance.height - 1, len(message) + len(inp) - 1)

    # Write the message to the screen
    instance.screen.addstr(instance.height - 1, 0, message, curses.color_pair(color))

    while True:
        # Wait for a keypress
        key = instance.screen.getch()

        # Subtracting a key (backspace)
        if key in (curses.KEY_BACKSPACE, 127, '\b'):
            # Write whitespace over characters to refresh it
            clear(instance, instance.height - 1, len(message) + len(inp) - 1)

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
            valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!/_-0123456789 "
            if chr(key) in valid and len(inp) < (instance.width - 2):
                inp.append(chr(key))

        # Refresh the screen
        instance.refresh()

        # Write the message to the screen
        instance.screen.addstr(instance.height - 1, 0, message, curses.color_pair(color))

        # Join the input together for visibility on the screen
        input_text = "".join(inp)

        # Write the input text to the screen
        instance.screen.addstr(instance.height - 1, len(message), input_text)


def press_key_to_continue(instance, message: str, color: int = None):
    # Hide the cursor
    cursors.mode("hidden")

    # Clear the bottom of the screen
    clear(instance, instance.height - 1, 0)

    # Write the entire message to the screen
    instance.screen.addstr(instance.height - 1, 0, message, curses.color_pair(color or 1))
    instance.screen.addstr(instance.height - 1, len(message) + 1, f"(press any key)")

    # Wait for a keypress
    instance.screen.getch()

    # Clear the bottom of the screen
    clear(instance, instance.height - 1, 0)

    # Show the cursor
    cursors.mode("visible")


def error(instance, message: str):
    # Parse the error message
    error_message = f"ERROR: {message}"

    # Create a prompt
    press_key_to_continue(instance, error_message, 3)


def fatal_error(exception: Exception):
    # End the curses session
    curses.endwin()

    # Print the error message and traceback
    print(f"{Col.red}FATAL ERROR:{Col.end} "
          f"{Col.yellow}{exception}{Col.end}\n")
    print(traceback.format_exc())

    # Exit, with an error exit code
    sys.exit(0)


def goodbye(instance):
    choice = prompt(instance, "Really quit lambda? (y/n): ", 11)
    if choice and choice[0] == "y":
        curses.endwin()
        sys.exit()

    else:
        clear(instance, instance.height - 1, 0)

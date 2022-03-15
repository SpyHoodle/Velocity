from sys import exit
import curses


def goodbye(stdscr, data):
    # The prompt message
    saved = "All changes are saved."
    prompt = "Really quit? (y or n): "

    # Clear the bottom line
    stdscr.addstr(data["height"] - 1, 0, " " * (data["width"] - 1), curses.color_pair(1))

    # Print the prompt
    stdscr.addstr(data["height"] - 1, 0, prompt, curses.color_pair(11))

    # Wait for and capture a key press from the user
    key = stdscr.getch()

    if key == ord("y"):
        # Only exit if the key was "y", a confirmation
        exit()

    # Clear the bottom line again
    stdscr.addstr(data["height"] - 1, 0, " " * (data["width"] - 1), curses.color_pair(1))


def error(stdscr, data, error_msg):
    # Print the error message to the bottom line
    error_msg = f"ERROR: {error_msg}"
    stdscr.addstr(data["height"] - 1, 0, error_msg, curses.color_pair(3))
    stdscr.addstr(data["height"] - 1, len(error_msg) + 1, "(press any key) ", curses.color_pair(1))

    # Wait for a key to be pressed
    stdscr.getch()

    # Clear the bottom line
    stdscr.addstr(data["height"] - 1, 0, " " * (data["width"] - 1), curses.color_pair(1))

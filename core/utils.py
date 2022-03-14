from sys import exit
import curses


def goodbye(stdscr, height, width):
    # The prompt message
    prompt = "Really quit lambda? (y or n): "

    # Clear the bottom line
    stdscr.addstr(height-1, 0, " " * (width - 1), curses.color_pair(1))
    
    # Print the prompt
    stdscr.addstr(height-1, 0, prompt, curses.color_pair(11))

    # Wait for and capture a key press from the user
    key = stdscr.getch()

    if key == ord("y"):
        # Only exit if the key was "y", a confirmation
        exit()

    # Clear the bottom line again
    stdscr.addstr(height-1, 0, " " * (width - 1), curses.color_pair(1))


def error(stdscr, height, error_msg):
    error_msg = f" ERROR {error_msg}"
    stdscr.addstr(height-1, 0, error_msg, curses.color_pair(3))

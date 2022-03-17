from sys import exit
import curses


def refresh_window_size(screen, data):
    # Get the height and width of the screen
    data["height"], data["width"] = screen.getmaxyx()

    # Return the data as changes may have been made
    return data


def clear_line(screen, data, line):
    # Clear the specified line
    screen.addstr(line, 0, " " * (data["width"] - 1), curses.color_pair(1))


def prompt(screen, data, text):
    # Print the prompt
    screen.addstr(data["height"] - 1, 0, text, curses.color_pair(11))

    # Wait for and capture a key press from the user
    return screen.getch()


def goodbye(screen, data):
    # Create a goodbye prompt
    key = prompt(screen, data, "Really quit? (y or n): ")

    # Clear the bottom line
    clear_line(screen, data, data["height"] - 1)

    if key == ord("y"):
        # Only exit if the key was "y", a confirmation
        exit()

    # Clear the bottom line again
    clear_line(screen, data, data["height"] - 1)


def error(screen, data, error_msg):
    # Print the error message to the bottom line
    error_msg = f"ERROR: {error_msg}"
    screen.addstr(data["height"] - 1, 0, error_msg, curses.color_pair(3))
    screen.addstr(data["height"] - 1, len(error_msg) + 1, "(press any key) ", curses.color_pair(1))

    # Wait for a key to be pressed
    screen.getch()

    # Clear the bottom line
    clear_line(screen, data, data["height"] - 1)

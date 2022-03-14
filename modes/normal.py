from modes import command
from modes import insert
from core import statusbar


def execute(stdscr, height, width, key, data):
    if key == ord("j"):
        # Move the cursor down
        data["cursor_y"] += 1

    elif key == ord("k"):
        # Move the cursor up
        data["cursor_y"] -= 1

    elif key == ord("l"):
        # Move the cursor right
        data["cursor_x"] += 1

    elif key == ord("h"):
        # Move the cursor left
        data["cursor_x"] -= 1

    elif key == ord("i"):
        # Insert mode
        data = insert.activate(stdscr, height, width, data)

    elif key in (ord(":"), ord(";")):
        # Switch to command mode
        data = command.activate(stdscr, height, width, data)

    return data


def activate(stdscr, height, width, data):
    # Refresh the status bar
    statusbar.refresh(stdscr, height, width, "NORMAL")

    # Wait for and capture a key press from the user
    key = stdscr.getch()

    # Check against the keybindings
    data = execute(stdscr, height, width, key, data)
    return data

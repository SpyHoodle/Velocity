from core import statusbar, cursor


def execute(data, key):
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
        # Exit normal mode and enter insert mode
        data["mode"] = "insert"

    elif key == ord("I"):
        # Exit normal mode and enter insert mode
        data["cursor_x"] += 1
        data["mode"] = "insert"

    elif key in (ord(":"), ord(";")):
        # Exit normal mode and enter command mode
        data["mode"] = "command"

    return data


def activate(stdscr, data):
    # Refresh the status bar
    statusbar.refresh(stdscr, data)

    # Move the cursor
    cursor.move(stdscr, data)

    # Switch the cursor to a block
    cursor.cursor_mode("block")

    # Wait for and capture a key press from the user
    key = stdscr.getch()

    # Check against the keybindings
    data = execute(data, key)

    return data

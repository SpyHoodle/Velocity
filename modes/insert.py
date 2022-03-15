from core import statusbar, cursor


def execute(data, key):
    return data


def activate(stdscr, data):
    # Refresh the status bar with a different colour for insert
    data["statusbar_colors"] = [8, 12, 14, 2]
    statusbar.refresh(stdscr, data)

    # Refresh the status bar
    statusbar.refresh(stdscr, data)

    # Move the cursor
    cursor.move(stdscr, data)

    # Switch to a line cursor
    cursor.cursor_mode("line")

    # Wait for and capture a key press from the user
    key = stdscr.getch()

    # Exit insert mode
    if key == 27:
        data["mode"] = "normal"
        return data

    # Check keybindings
    data = execute(data, key)

    return data

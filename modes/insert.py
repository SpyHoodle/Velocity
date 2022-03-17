from core import statusbar, cursor


def execute(data, key):
    return data


def activate(screen, data):
    # Refresh the status bar with a different colour for insert
    data["statusbar_colors"] = [8, 12, 14, 2]
    statusbar.refresh(screen, data)

    # Refresh the status bar
    statusbar.refresh(screen, data)

    # Move the cursor
    cursor.move(screen, data)

    # Switch to a line cursor
    cursor.cursor_mode("line")

    # Wait for and capture a key press from the user
    key = screen.getch()

    # Exit insert mode
    if key == 27:
        data["mode"] = "normal"
        return data

    # Check keybindings
    data = execute(data, key)

    return data

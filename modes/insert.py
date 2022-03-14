from core import statusbar


def execute(stdscr, height, width, key):
    return


def activate(stdscr, height, width, data):
    # Refresh the status bar with a different colour for insert
    colors = [8, 12, 14, 2]
    statusbar.refresh(stdscr, height, width, "INSERT", colors)

    while True:
        # Wait for and capture a key press from the user
        key = stdscr.getch()

        return data

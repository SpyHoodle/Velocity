import curses


def cursor_mode(mode):
    if mode == "block":
        print("\033[2 q")

    elif mode == "line":
        print("\033[6 q")

    elif mode == "hidden":
        curses.curs_set(0)

    elif mode == "visible":
        curses.curs_set(1)


def cursor_push(cursor: list, direction: (int, str)) -> list:
    if direction in (0, "up", "north"):
        # Decrease the y position
        cursor[0] -= 1

    elif direction in (1, "right", "east"):
        # Increase the x position
        cursor[1] += 1

    elif direction in (2, "down", "south"):
        # Increase the y position
        cursor[0] += 1

    elif direction in (3, "left", "west"):
        # Decrease the x position
        cursor[1] -= 1

    return cursor


def cursor_move(screen, cursor: list):
    # Moves the cursor to anywhere on the screen
    screen.move(cursor[0], cursor[1])

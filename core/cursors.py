import curses


def cursor_mode(mode: str):
    if mode == "block":
        print("\033[2 q")

    elif mode == "line":
        print("\033[6 q")

    elif mode == "hidden":
        curses.curs_set(0)

    elif mode == "visible":
        curses.curs_set(1)


def cursor_push(instance, direction: (int, str)):
    if direction in (0, "up", "north"):
        # Decrease the y position
        instance.cursor[0] -= 1

    elif direction in (1, "right", "east"):
        # Increase the x position
        instance.cursor[1] += 1

    elif direction in (2, "down", "south"):
        # Increase the y position
        instance.cursor[0] += 1

    elif direction in (3, "left", "west"):
        # Decrease the x position
        instance.cursor[1] -= 1


def check_cursor(instance, cursor: list):
    cursor[1] = max(2, cursor[1])
    cursor[1] = min(instance.width - 1, cursor[1])
    cursor[0] = max(0, cursor[0])
    cursor[0] = min(instance.height - 2 - len(instance.components.components["bottom"]), cursor[0])

    return cursor


def cursor_move(instance):
    # Run a final check to see if the cursor is valid
    instance.cursor = check_cursor(instance, instance.cursor)

    # Moves the cursor to anywhere on the screen
    instance.screen.move(instance.cursor[0], instance.cursor[1])

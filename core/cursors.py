import curses


def mode(to_mode: str):
    if to_mode == "block":
        print("\033[2 q")

    elif to_mode == "line":
        print("\033[6 q")

    elif to_mode == "hidden":
        curses.curs_set(0)

    elif to_mode == "visible":
        curses.curs_set(1)


def push(instance, direction: (int, str)):
    if direction in (0, "up", "north"):
        # If the cursor isn't at the top of the screen
        if instance.raw_cursor[0] > 0:
            # Move the cursor up
            instance.raw_cursor[0] -= 1

        # Move the buffer upwards if the cursor is at the top of the screen and not at the top of the buffer
        if instance.raw_cursor[0] == 0 and instance.cursor[0] == instance.offset[0] and instance.cursor[0] != 0:
            instance.offset[0] -= 1

    elif direction in (2, "down", "south"):
        if instance.raw_cursor[0] == instance.safe_height and instance.cursor[0] != len(instance.buffer.data) - 1:
            instance.offset[0] += 1

        # If the cursor isn't at the bottom of the screen
        elif instance.raw_cursor[0] != instance.safe_height and instance.cursor[0] != len(instance.buffer.data) - 1:
            # Move the cursor down
            instance.raw_cursor[0] += 1

    elif direction in (1, "right", "east"):
        # Move the cursor one to the right
        instance.raw_cursor[1] += 1

    elif direction in (3, "left", "west"):
        # Move the cursor one to the left
        instance.raw_cursor[1] -= 1


def check(instance, cursor: list) -> list:
    # Prevent the cursor from going outside the buffer
    cursor[1] = min(len(instance.buffer.data[instance.cursor[0]]) - 1, cursor[1])

    # Prevent any negative values
    cursor[0] = max(0, cursor[0])
    cursor[1] = max(0, cursor[1])

    # Prevent the cursor from going outside the screen
    cursor[1] = min(instance.safe_width, cursor[1])
    cursor[0] = min(instance.safe_height, cursor[0])

    return cursor


def move(instance):
    # Run a final check to see if the cursor is valid
    instance.raw_cursor = check(instance, instance.raw_cursor)

    # Moves the cursor to anywhere on the screen
    instance.screen.move(instance.raw_cursor[0], instance.raw_cursor[1] +
                         instance.components.get_component_width(instance.components.components["left"]))

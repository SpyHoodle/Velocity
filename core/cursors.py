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
        # If the cursor is at the top of the file
        if instance.cursor[0] == 0 and not instance.offset[0] == 0:
            # Move the buffer up
            instance.offset[0] -= 1

        elif instance.cursor[0] != 0:
            # Decrease the y position of the cursor
            instance.cursor[0] -= 1

            # Jump to the end of the line
            if instance.cursor[1] > len(instance.buffer.data[instance.current_line - 1]) - 2:
                instance.cursor[1] = len(instance.buffer.data[instance.current_line - 1]) - 2

    elif direction in (1, "right", "east"):
        # Increase the x position of the cursor
        if instance.cursor[1] < len(instance.buffer.data[instance.current_line]) - 2:
            instance.cursor[1] += 1

    elif direction in (2, "down", "south"):
        # Check if the cursor is at the bottom of the screen
        if instance.cursor[0] == instance.safe_height - 2 and not instance.current_line == len(instance.buffer.data):
            # Move the buffer down
            instance.offset[0] += 1

        elif instance.cursor[0] != instance.safe_height - 2:
            # Increase the y position of the cursor
            instance.cursor[0] += 1

            # Jump to the end of the line
            if instance.cursor[1] > len(instance.buffer.data[instance.current_line + 1]) - 2:
                instance.cursor[1] = len(instance.buffer.data[instance.current_line + 1]) - 2

    elif direction in (3, "left", "west"):
        # Decrease the x position of the cursor
        if instance.cursor[1] != 0:
            instance.cursor[1] -= 1


def check(instance, cursor: list):
    # Prevent any values out of bounds (especially important when resizing)
    cursor[1] = max(0, cursor[1])
    cursor[1] = min(instance.safe_width - 1, cursor[1])
    cursor[0] = max(0, cursor[0])
    cursor[0] = min(instance.height - 2 - len(instance.components.components["bottom"]), cursor[0])

    return cursor


def move(instance):
    # Run a final check to see if the cursor is valid
    instance.cursor = check(instance, instance.cursor)

    # Moves the cursor to anywhere on the screen
    instance.screen.move(instance.cursor[0], instance.cursor[1] +
                         instance.components.get_component_width(instance.components.components["left"]))

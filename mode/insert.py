import curses

from core import cursors, modes, utils


def execute(instance, key):
    if key == 27:  # Escape
        # Switch to normal mode
        modes.activate(instance, "normal")

    elif key == 127:  # Backspace
        if instance.cursor[1] > 0:
            # Delete the character before the cursor
            instance.buffer.remove_char(instance)

            # Move the cursor one to the left
            cursors.push(instance, 3)

    else:
        # Insert the character
        instance.buffer.insert_char(instance, chr(key))

        # Move the cursor one to the right
        cursors.push(instance, 1)


def activate():
    # Switch the cursor to a line
    cursors.mode("line")

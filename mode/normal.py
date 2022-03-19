from core import cursors, modes
from mode import insert
from mode import command


def execute(instance, key):
    if key == ord("j"):
        # Move the cursor down
        instance.cursor = cursors.cursor_push(instance.cursor, "down")

    elif key == ord("k"):
        # Move the cursor up
        instance.cursor = cursors.cursor_push(instance.cursor, "up")

    elif key == ord("l"):
        # Move the cursor right
        instance.cursor = cursors.cursor_push(instance.cursor, "right")

    elif key == ord("h"):
        # Move the cursor left
        instance.cursor = cursors.cursor_push(instance.cursor, "left")

    elif key == ord("i"):
        # Activate insert mode
        modes.activate(instance, "insert")

    elif key == ord("I"):
        # Move the cursor to the right
        instance.cursor = cursors.cursor_push(instance.cursor, "right")

        # Then activate insert mode
        modes.activate(instance, "insert")

    elif key in (ord(":"), ord(";")):
        # Activate command mode
        modes.activate(instance, "command")


def activate():
    # Switch the cursor to a block
    cursors.cursor_mode("block")

from core import cursors, modes
from mode import insert
from mode import command


def execute(instance, key):
    if key == ord("j"):
        # Move the cursor down
        cursors.cursor_push(instance, "down")

    elif key == ord("k"):
        # Move the cursor up
        cursors.cursor_push(instance, "up")

    elif key == ord("l"):
        # Move the cursor right
        cursors.cursor_push(instance, "right")

    elif key == ord("h"):
        # Move the cursor left
        cursors.cursor_push(instance, "left")

    elif key == ord("i"):
        # Activate insert mode
        modes.activate(instance, "insert")

    elif key == ord("I"):
        # Move the cursor to the right
        cursors.cursor_push(instance, "right")

        # Then activate insert mode
        modes.activate(instance, "insert")

    elif key in (ord(":"), ord(";")):
        # Activate command mode
        modes.activate(instance, "command")


def activate():
    # Switch the cursor to a block
    cursors.cursor_mode("block")

import curses

from core import cursors, modes, utils


def execute(instance, key):
    if key == curses.BUTTON1_CLICKED:
        # Move the cursor to the position clicked
        utils.prompt(instance, str(curses.getmouse()))

    elif key in (ord("j"), curses.KEY_DOWN):
        # Move the cursor down
        cursors.push(instance, "down")

    elif key in (ord("k"), curses.KEY_UP):
        # Move the cursor up
        cursors.push(instance, "up")

    elif key in (ord("l"), curses.KEY_RIGHT):
        # Move the cursor right
        cursors.push(instance, "right")

    elif key in (ord("h"), curses.KEY_LEFT):
        # Move the cursor left
        cursors.push(instance, "left")

    elif key == ord("i"):
        # Activate insert mode
        modes.activate(instance, "insert")

    elif key == ord("I"):
        # Move the cursor to the right
        cursors.push(instance, "right")

        # Then activate insert mode
        modes.activate(instance, "insert")

    elif key in (ord(":"), ord(";")):
        # Activate command mode
        modes.activate(instance, "command")


def activate():
    # Switch the cursor to a block
    cursors.mode("block")

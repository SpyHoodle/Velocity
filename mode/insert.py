from core import cursors
from mode import normal


def execute(instance, key):
    if key == 27:
        # Switch to normal mode
        instance.mode = "normal"
        normal.activate(instance)

    return instance


def activate(instance):
    # Switch the cursor to a line
    cursors.cursor_mode("line")

    return instance

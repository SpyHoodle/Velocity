from mode import normal, insert, command


def activate(instance, mode):
    # Visibly update the mode
    instance.mode = mode

    # Refresh the screen
    instance.refresh()

    if mode == "command":
        # Activate command mode
        command.activate(instance)

    elif mode == "insert":
        # Activate insert mode
        insert.activate()

    elif mode == "normal":
        # Activate normal mode
        normal.activate()


def handle_key(instance, key):
    # Normal mode - default keybindings
    if instance.mode == "normal":
        normal.execute(instance, key)

    # Insert mode - inserting text to the buffer
    elif instance.mode == "insert":
        insert.execute(instance, key)

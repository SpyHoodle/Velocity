from mode import normal, insert, command


def activate(instance, mode):
    # Visibly update the mode
    instance.mode = mode

    # Refresh the screen
    instance.refresh()

    if mode == "command":
        # Activate command mode
        instance.components.components["bottom"][0].colors[1] = 5
        command.activate(instance)

    elif mode == "insert":
        # Activate insert mode
        instance.components.components["bottom"][0].colors[1] = 9
        insert.activate()

    elif mode == "normal":
        # Activate normal mode
        instance.components.components["bottom"][0].colors[1] = 5
        normal.activate()


def handle_key(instance, key):
    # Normal mode - default keybindings
    if instance.mode == "normal":
        normal.execute(instance, key)

    # Insert mode - inserting text to the buffer
    elif instance.mode == "insert":
        insert.execute(instance, key)

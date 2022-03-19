from mode import normal, insert, command


def activate(instance, mode) -> object:
    # Visibly update the mode
    instance.mode = mode
    instance.update()

    if mode == "command":
        instance = command.activate(instance)

    elif mode == "insert":
        instance = insert.activate(instance)

    elif mode == "normal":
        instance = normal.activate(instance)

    return instance


def handle_key(instance, key):
    if instance.mode == "normal":
        instance = normal.execute(instance, key)

    # Insert mode - inserting text to the buffer
    elif instance.mode == "insert":
        instance = insert.execute(instance, key)

    # Command mode - extra commands for lambda
    elif instance.mode == "command":
        instance = command.activate(instance)

    return instance

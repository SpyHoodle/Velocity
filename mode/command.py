from core import utils


def execute(instance, commands):
    if not commands:
        # Quit if there are no commands, don't check anything
        return instance

    for command in commands:
        if command == "w":
            # Write to the file
            pass

        elif command == "q":
            # Load a goodbye prompt
            utils.goodbye(instance)

        else:
            utils.error(instance, f"not an editor command: '{command}'")

    return instance


def activate(instance):
    # Start the prompt
    commands = utils.prompt(instance, ":")

    # Execute the commands
    instance = execute(instance, commands)

    # Return to normal mode
    instance.mode = "normal"

    return instance

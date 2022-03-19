from core import utils


def execute(instance, commands):
    # Only if commands are given
    if commands:
        # Check each command in the list of commands
        for command in commands:
            # Write
            if command == "w":
                # Write to the file
                pass

            # Quit
            elif command == "q":
                # Load a goodbye prompt
                utils.goodbye(instance)

            # Unknown command
            else:
                utils.error(instance, f"not an editor command: '{command}'")


def activate(instance):
    # Create a prompt, which returns the input (commands)
    commands = utils.prompt(instance, ":")

    # Execute the commands given
    execute(instance, commands)

    # Return to normal mode once all commands are executed
    instance.mode = "normal"

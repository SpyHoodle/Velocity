from core import utils


def execute(instance, commands: list):
    # Only if commands are given
    if commands:
        # Check each command in the list of commands
        for command in commands:
            if command == "w":  # Write
                # Write to the file
                pass

            if command == "d":  # Debug
                # Create the debug prompt
                utils.prompt(instance, f"*Whawt awe uwu doing tuwu me mastew?* "
                                       f"Cursor: {instance.cursor} Raw: {instance.raw_cursor} "
                                       f"Len: {len(instance.buffer.data)}")

            elif command == "q":  # Quit
                # Create a goodbye prompt
                utils.goodbye(instance)

            else:  # Invalid command
                utils.error(instance, f"invalid command: '{command}'")


def activate(instance):
    # Create a prompt, which returns the input (commands)
    commands = utils.prompt(instance, ":")

    # Execute the commands given
    execute(instance, commands)

    # Return to normal mode once all commands are executed
    instance.mode = "normal"

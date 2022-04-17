from core import utils


def execute(instance, commands: list):
    # Only if commands are given
    if commands:
        # Check each command in the list of commands
        for command in commands:
            if command == "d":  # Debug
                # Create the debug prompt
                utils.press_key_to_continue(instance, f"Cursor: {instance.cursor} Raw: {instance.raw_cursor} "
                                                      f"Len: {len(instance.buffer.data)}")

            elif command == "t":  # Toggle
                # Toggle the status bar theme
                if instance.components.components["bottom"][0].theme == "default":
                    instance.components.components["bottom"][0].theme = "inverted"
                else:
                    instance.components.components["bottom"][0].theme = "default"

            elif command == "w":  # Write
                # Write to the file
                utils.save_file(instance, instance.buffer.path, instance.buffer.data)

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

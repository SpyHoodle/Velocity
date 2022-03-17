from core import statusbar, utils
import curses


def execute(screen, data, commands):
    if not commands:
        # Quit if there are no commands, don't check anything
        return data

    for command in commands:
        if command == "w":
            # Write to the file
            pass

        elif command == "q":
            # Goodbye prompt
            utils.goodbye(screen, data)

        elif command == "t":
            # Theme switcher
            if data["statusbar_theme"] == "filled":
                data["statusbar_theme"] = "bare"

            else:
                data["statusbar_theme"] = "filled"

        else:
            utils.error(screen, data, f"Not an editor command: '{command}'")

    return data


def activate(screen, data):
    # Initialise variables
    commands = []

    # Visibly switch to command mode
    statusbar.refresh(screen, data)
    screen.addstr(data["height"]-1, 0, ":")
    screen.move(data["height"]-1, 1)

    # Main loop
    while True:
        # Get a key inputted by the user
        key = screen.getch()

        # Handle subtracting a key (backspace)
        if key == curses.KEY_BACKSPACE:
            # Write whitespace over characters to refresh it
            screen.addstr(data["height"]-1, 1, " " * len(commands))

            if commands:
                # Subtract a character
                commands.pop()
            else:
                # Exit command mode and enter normal mode if there is nothing left
                data["mode"] = "normal"
                return data

        elif key == 27:
            # Exit command mode and enter normal mode if "esc" is pressed
            data["mode"] = "normal"
            return data

        elif key in (curses.KEY_ENTER, ord('\n'), ord('\r'), ord(":"), ord(";")):
            # Execute commands
            data = execute(screen, data, commands)

            # Clear the bottom bar
            screen.addstr(data["height"] - 1, 0, " " * (data["width"] - 1))

            # Return to normal mode after executing a command
            data["mode"] = "normal"
            return data

        else:
            # If any other key is typed, append it
            # As long as the key is in the valid list
            valid = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ!"
            if chr(key) in valid and len(commands) < (data["width"] - 2):
                commands.append(chr(key))

        # Join the commands together for visibility on the screen
        friendly_command = "".join(commands)

        # Write the commands to the screen
        screen.addstr(data["height"]-1, 1, friendly_command)

        # Move the cursor the end of the commands
        screen.move(data["height"]-1, len(commands)+1)

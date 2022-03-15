from core import statusbar, utils
import curses


def execute(stdscr, data, commands):
    if not commands:
        # Quit if there are no commands, don't check anything
        return

    for command in commands:
        if command == "w":
            # Write to the file
            pass

        elif command == "q":
            # Goodbye prompt
            utils.goodbye(stdscr, data)

        elif command == "t":
            if data["statusbar_theme"] == "filled":
                data["statusbar_theme"] = "bare"

            else:
                data["statusbar_theme"] = "filled"

        else:
            utils.error(stdscr, data, f"Not an editor command: '{command}'")

    return data


def activate(stdscr, data):
    # Initialise variables
    commands = []

    # Visibly switch to command mode
    statusbar.refresh(stdscr, data)
    stdscr.addstr(data["height"]-1, 0, ":")
    stdscr.move(data["height"]-1, 1)

    # Main loop
    while True:
        # Get a key inputted by the user
        key = stdscr.getch()

        # Handle subtracting a key (backspace)
        if key == curses.KEY_BACKSPACE:
            # Write whitespace over characters to refresh it
            stdscr.addstr(data["height"]-1, 1, " " * len(commands))

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
            data = execute(stdscr, data, commands)

            # Clear the bottom bar
            stdscr.addstr(data["height"] - 1, 0, " " * (data["width"] - 1))

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
        stdscr.addstr(data["height"]-1, 1, friendly_command)

        # Move the cursor the end of the commands
        stdscr.move(data["height"]-1, len(commands)+1)

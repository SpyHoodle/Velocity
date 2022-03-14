from core import statusbar, utils
import curses


def execute(stdscr, height, width, commands):
    if not commands:
        # Quit if there are no commands, don't check anything
        return

    for command in commands:
        if command == "w":
            # Write to the file
            pass
        elif command == "q":
            # Goodbye prompt
            utils.goodbye(stdscr, height, width)


def activate(stdscr, height, width, data):
    # Initialise variables
    key = 0
    commands = []

    # Visibly switch to command mode
    statusbar.refresh(stdscr, height, width, "COMMAND")
    stdscr.addstr(height-1, 0, ":")
    stdscr.move(height-1, 1)

    # Main loop
    while True:
        # Get a key inputted by the user
        key = stdscr.getch()

        # Handle subtracting a key (backspace)
        if key == curses.KEY_BACKSPACE:
            # Write whitespace over characters to refresh it
            stdscr.addstr(height-1, 1, " " * len(commands))

            if commands:
                # Subtract a character
                commands.pop()
            else:
                # If there's nothing left, quit the loop
                return data

        elif key == 27:
            # Quit the loop if escape is pressed
            return data

        elif key in (curses.KEY_ENTER, ord('\n'), ord('\r')):
            # Execute commands
            execute(stdscr, height, width, commands)

            # Clear the bottom bar
            stdscr.addstr(height - 1, 0, " " * (width - 1))

            return data

        else:
            # If any other key is typed, append it
            # As long as the key is in the valid list
            valid = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ!"
            if chr(key) in valid and len(commands) < (width - 2):
                commands.append(chr(key))

        # Join the commands together for visibility on the screen
        friendly_command = "".join(commands)
        # Write the commands to the screen
        stdscr.addstr(height-1, 1, friendly_command)
        # Move the cursor the end of the commands
        stdscr.move(height-1, len(commands)+1)

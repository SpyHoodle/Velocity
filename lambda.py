from core import colors, cursor, mode, files, buffer, welcome
import os
import curses
import argparse


def start(screen, buffer_name, buffer_list):
    # Initialise data before starting
    data = {
        "cursor_y": 0,
        "cursor_x": 0,
        "height": 0,
        "width": 0,
        "mode": "normal",
        "icon": "λ",
        "info_bar": ["  "],
        "buffer_name": buffer_name,
        "buffer_list": buffer_list,
        "visible_y": 0,
        "visible_x": 0,
        "statusbar_theme": "filled"
    }

    # Initialise colors
    colors.init_colors()

    # Change the cursor shape
    cursor.cursor_mode("block")

    # Start the screen
    if data["buffer_name"] == "[No Name]":
        welcome.start_screen(screen)

    # Main loop
    while True:
        # Get the height and width of the screen
        data["height"], data["width"] = screen.getmaxyx()

        # Write the buffer to the screen
        buffer.write_buffer(screen, data)

        # Activate the next mode
        data = mode.activate(screen, data)

        # Write the buffer to the screen
        buffer.write_buffer(screen, data)

        # Refresh and clear the screen
        screen.refresh()
        screen.clear()

        # Write the buffer to the screen
        buffer.write_buffer(screen, data)


def main():
    # Arguments
    parser = argparse.ArgumentParser(description="Next generation hackable text editor for nerds.")
    parser.add_argument("file", metavar="file", type=str, nargs="?",
                        help="The name of a file for lambda to open")

    # Collect the arguments
    args = parser.parse_args()

    # Check if a file name has actually been inputted
    if args.file:
        # Set the buffer name
        buffer_name = os.path.basename(args.file)

        # Only if the file exists
        if os.path.exists(args.file):
            # Load the file into the buffer
            buffer_list = files.open_file(args.file)

            # Convert each line into a list of lists with each element of the sublist representing one character
            for index, line in enumerate(buffer_list):
                buffer_list[index] = list(line)

        else:
            # New file being created, no content
            buffer_list = [[""]]

    else:
        # Buffer has no name
        buffer_name = "[No Name]"

        # Buffer has no value
        buffer_list = [[""]]

    # Change the escape delay to 25ms
    # Fixes an issue where esc takes way too long to press
    os.environ.setdefault("ESCDELAY", "25")

    # Initialise the screen
    curses.wrapper(start, buffer_name, buffer_list)


if __name__ == "__main__":
    main()

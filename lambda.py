from core import colors, cursor, mode, files, buffer
import os
import curses
import argparse


def start_screen(stdscr):
    # Get window height and width
    height, width = stdscr.getmaxyx()

    # Startup text
    title = "λ Lambda"
    subtext = [
        "Next generation hackable text editor for nerds",
        "",
        "Type :h to open the README.md document",
        "Type :o <file> to open a file and edit",
        "Type :q or <C-c> to quit lambda.py"
    ]

    # Centering calculations
    start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
    start_y = int((height // 2) - 2)

    # Rendering title
    stdscr.addstr(start_y, start_x_title, title, curses.color_pair(7) | curses.A_BOLD)

    # Print the subtext
    for text in subtext:
        start_y += 1
        start_x = int((width // 2) - (len(text) // 2) - len(text) % 2)
        stdscr.addstr(start_y, start_x, text)


def start(stdscr, buffer_name, buffer_list):
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
        "statusbar_theme": "filled"
    }

    # Initialise colors
    colors.init_colors()

    # Change the cursor shape
    cursor.cursor_mode("block")

    # Start the screen
    if data["buffer_name"] == "[No Name]":
        start_screen(stdscr)

    # Main loop
    while True:
        # Get the height and width of the screen
        data["height"], data["width"] = stdscr.getmaxyx()

        # Write the buffer to the screen
        buffer.write_buffer(stdscr, data)

        # Activate the next mode
        data = mode.activate(stdscr, data)

        # Refresh and clear the screen
        stdscr.refresh()
        stdscr.clear()


def main():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("file", metavar="file", type=str, nargs="?",
                        help="File to open")

    args = parser.parse_args()
    # Check if a file name has been inputted
    if args.file:
        buffer_name = args.file
        buffer_list = files.open_file(buffer_name)

        # Convert each line into a list of lists with each element of the sublist representing one character
        for index, line in enumerate(buffer_list):
            buffer_list[index] = list(line)

    else:
        buffer_name = "[No Name]"
        buffer_list = [[""]]

    # Change the escape delay to 25ms
    # Fixes an issue where esc takes too long to press
    os.environ.setdefault("ESCDELAY", "25")

    # Initialise the screen
    curses.wrapper(start, buffer_name, buffer_list)


if __name__ == "__main__":
    main()

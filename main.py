from core import colors, cursors, buffers, modes, utils
from core.buffers import Buffer
from core.components import Components
import traceback
import argparse
import curses
import sys
import os


class Lambda:
    def __init__(self, buffer: Buffer):
        self.screen = curses.initscr()
        self.buffer = buffer
        self.cursor = [0, 0]
        self.mode = "normal"
        self.components = Components()
        self.height = self.screen.getmaxyx()[0]
        self.width = self.screen.getmaxyx()[1]
        self.safe_height = self.height - len(self.components.components["bottom"])
        self.config = {"icon": "λ"}

    def update_dimensions(self):
        self.height, self.width = self.screen.getmaxyx()
        self.safe_height = self.height - len(self.components.components["bottom"])

    def update(self):
        # Update the dimensions
        self.update_dimensions()

        # Refresh the on-screen components
        self.components.render(self)

        # Move the cursor
        cursors.cursor_move(self.screen, self.cursor)

    def start(self):
        # Initialise colors
        colors.init_colors()

        # Change the cursor shape
        cursors.cursor_mode("block")

        # Turn no echo on
        curses.noecho()

        # Show a welcome message if lambda opens with no file
        if not self.buffer.path:
            utils.welcome(self.screen)

        # Main loop
        self.run()

    def run(self):
        while True:
            # Write the buffer to the screen
            # buffers.write_buffer(screen, buffer)

            # Update the screen
            self.update()

            # Wait for a keypress
            key = self.screen.getch()

            # Handle the key
            modes.handle_key(self, key)

            # Refresh and clear the screen
            self.screen.refresh()
            self.screen.clear()


def main():
    # Command line arguments
    parser = argparse.ArgumentParser(description="Next generation hackable text editor for nerds.")
    parser.add_argument("file", metavar="file", type=str, nargs="?",
                        help="The name of a file for lambda to open")

    # Collect the arguments passed into lambda
    args = parser.parse_args()

    # Load the file into buffer
    buffer = buffers.load_file(args.file)

    # Change the escape delay to 25ms
    # Fixes an issue where esc takes way too long to press
    os.environ.setdefault("ESCDELAY", "25")

    # Load lambda with the buffer
    screen = Lambda(buffer)

    # Start the screen
    try:
        screen.start()

    # KeyboardInterrupt is thrown when ctrl+c is pressed
    except KeyboardInterrupt:
        curses.endwin()
        sys.exit()

    except Exception as exception:
        curses.endwin()
        print(f"{colors.Codes.red}FATAL ERROR:{colors.Codes.end} "
              f"{colors.Codes.yellow}{exception}{colors.Codes.end}\n")
        print(traceback.format_exc())
        sys.exit(0)


if __name__ == "__main__":
    main()

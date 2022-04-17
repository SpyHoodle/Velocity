import argparse
import curses
import os

from core import colors, cursors, buffers, modes, utils
from core.buffers import Buffer
from core.components import Components


class Lambda:
    def __init__(self, buffer: Buffer = None, config: dict = None):
        self.cursor = [0, 0]
        self.raw_cursor = [0, 0]
        self.offset = [0, 0]
        self.height = 0
        self.width = 0
        self.safe_height = 0
        self.safe_width = 0
        self.mode = "normal"
        self.config = config or {"icon": "λ"}
        self.buffer = buffer or [""]
        self.screen = curses.initscr()
        self.components = Components(self)

    def update_dimensions(self):
        # Calculate the entire height and width of the terminal
        self.height, self.width = self.screen.getmaxyx()

        # Calculate the safe area for the buffer by removing heights & widths of components
        self.safe_height = self.height - len(self.components.components["bottom"]) - 2
        self.safe_width = self.width - self.components.get_component_width(self.components.components["left"]) - 1

    def refresh(self):
        # Calculate the cursor position in the file
        self.cursor[0], self.cursor[1] = self.raw_cursor[0] + self.offset[0], self.raw_cursor[1] + self.offset[1]

        # Update the dimensions of the terminal
        self.update_dimensions()

        # Write the buffer to the screen
        self.buffer.render(self)

        # Refresh the on-screen components
        self.components.render(self)

        # Move the cursor
        cursors.move(self)

    def start(self):
        # Change the escape key delay to 25ms
        # Fixes an issue where the "esc" key takes way too long to press
        os.environ.setdefault("ESCDELAY", "25")

        # Initialise colors
        colors.init_colors()

        # Change the cursor shape
        cursors.mode("block")

        # Don't echo any key-presses
        curses.noecho()

        # Show a welcome message if lambda opens with no file
        if not self.buffer.path:
            utils.welcome(self.screen)

        # Main loop
        self.run()

    def run(self):
        # The main loop, which runs until the user quits
        while True:
            # Update the screen variables
            self.refresh()

            # Wait for a keypress
            key = self.screen.getch()

            # Handle the key
            modes.handle_key(self, key)

            # Refresh and clear the screen
            self.screen.refresh()
            self.screen.erase()


def main():
    # Shell arguments
    parser = argparse.ArgumentParser(description="Next generation hackable text editor for nerds.")
    parser.add_argument("file", metavar="file", type=str, nargs="?",
                        help="The name of a file for lambda to open")

    # Collect the arguments passed into lambda at the shell
    args = parser.parse_args()

    # Load the file into a Buffer object
    buffer = buffers.load_file(args.file)

    # Load the config
    config = utils.load_config()

    # Load lambda with the buffer object
    screen = Lambda(buffer, config)

    # Start the screen, this will loop until exit
    try:
        screen.start()

    # KeyboardInterrupt is thrown when <C-c> is pressed (exit)
    except KeyboardInterrupt:
        utils.gracefully_exit()

    # Excepts *any* errors that occur
    except Exception as exception:
        utils.fatal_error(exception)


if __name__ == "__main__":
    main()

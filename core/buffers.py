import os


class Buffer:
    def __init__(self, path: str, name: str = None, data: list = None):
        self.path = path
        self.name = name or "[No Name]"
        self.data = data or [""]

    def render(self, instance):
        for y, line in enumerate(self.data[instance.offset[0]:]):
            if y <= instance.safe_height:
                for x, character in enumerate(line[instance.offset[1]:]):
                    if x <= instance.safe_width:
                        instance.screen.addstr(y, x + instance.components.get_component_width(
                            instance.components.components["left"]), character)

                # Write blank spaces for the rest of the line
                if instance.safe_width - len(line) > 0:
                    instance.screen.addstr(y, instance.components.get_component_width(
                        instance.components.components["left"]) + len(line), " " * (instance.safe_width - len(line)))

    @staticmethod
    def delete_line(instance, y: int = None):
        # Default to the cursor position
        y = y or instance.cursor[0]

        # Remove a line from the buffer
        instance.buffer.data.pop(y)

    @staticmethod
    def insert_line(instance, y: int = None):
        # Default to the cursor position
        y = y or instance.cursor[0]

        # Insert a line into the buffer
        instance.buffer.data.insert(y, "")

    @staticmethod
    def delete_char(instance, y: int = None, x: int = None):
        # Default to the cursor position
        y = y or instance.cursor[0]
        x = x or instance.cursor[1]

        # Remove a character from the line at a given index
        instance.buffer.data[y] = instance.buffer.data[y][:x - 1] + instance.buffer.data[y][x:]

    @staticmethod
    def insert_char(instance, char: (str, chr), y: int = None, x: int = None):
        # Default to the cursor position
        y = y or instance.cursor[0]
        x = x or instance.cursor[1]

        # Insert a character into the line at a given index
        instance.buffer.data[y] = instance.buffer.data[y][:x] + char + instance.buffer.data[y][x:]


def open_file(file_path):
    # Open the file
    with open(file_path) as f:
        # Convert it into a list of lines
        lines = f.readlines()

    # Add a line if the file is empty or if the last line is not empty
    if lines[-1].endswith("\n") or not len(lines):
        lines.append("")

    # Remove the newlines
    lines = [line.rstrip("\n") for line in lines]

    # Return the list of lines
    return lines


def load_file(file_path=None):
    # Default settings for a file
    file_name = "[No Name]"
    file_data = [""]

    if file_path:
        # Set the file's name
        file_name = os.path.basename(file_path)

        # Only if the file actually exists
        if os.path.exists(file_path):
            # Open the file as a list of lines
            file_data = open_file(file_path)

    # Return a dictionary which will become all the data about the buffer
    return Buffer(file_path, file_name, file_data)

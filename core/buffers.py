import os


class Buffer:
    def __init__(self, path: str, name: str = None, data: list = None):
        self.path = path
        self.name = name or "[No Name]"
        self.data = data or [[""]]

    @staticmethod
    def remove_char(string: str, index: int) -> str:
        # Remove a character from a string at a given index
        return string[:index] + string[index + 1:]

    @staticmethod
    def insert_char(string: str, index: int, char: (str, chr)) -> str:
        # Insert a character into a string at a given index
        return string[:index] + char + string[index:]


def open_file(file_name):
    # Open the file
    with open(file_name) as f:
        # Convert it into a list of lines
        lines = f.readlines()

    # Return the list of lines
    return lines


def load_file(file_path=None):
    # Default settings for a file
    file_name = "[No Name]"
    file_data = [[""]]

    if file_path:
        # Set the file's name
        file_name = os.path.basename(file_path)

        # Only if the file actually exists
        if os.path.exists(file_path):
            # Open the file as a list of lines
            file_data = open_file(file_name)

    # Return a dictionary which will become all the data about the buffer
    return Buffer(file_path, file_name, file_data)

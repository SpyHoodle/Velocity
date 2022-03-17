def open_file(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    return lines

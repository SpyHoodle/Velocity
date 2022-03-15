def open_file(file):
    with open(file) as f:
        lines = f.readlines()
        return lines

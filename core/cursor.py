from core import utils, buffer


def cursor_mode(mode):
    if mode == "block":
        print("\033[2 q")

    elif mode == "line":
        print("\033[6 q")

    elif mode == "hidden":
        print('\033[? 25l')

    elif mode == "visible":
        print('\033[? 25h')


def check_cursor(data):
    if data["cursor_y"] + data["visible_y"] == len(data["buffer_list"]):
        data["cursor_y"] -= 1

    if data["cursor_y"] == data["height"] - 2 and not data["cursor_y"] + data["visible_y"] == len(data["buffer_list"]):
        data["visible_y"] += 1

    elif data["cursor_y"] == 0 and data["buffer_list"][data["visible_y"]] != data["buffer_list"][0]:
        data["visible_y"] -= 1

    elif data["cursor_x"] > len(data["buffer_list"][data["cursor_y"]]):
        data["cursor_x"] = len(data["buffer_list"][data["cursor_y"]])

    data["cursor_x"] = max(2, data["cursor_x"])
    data["cursor_x"] = min(data["width"] - 1, data["cursor_x"])
    data["cursor_y"] = max(0, data["cursor_y"])
    data["cursor_y"] = min(data["height"] - 3, data["cursor_y"])

    return data


def move(screen, data):
    # Calculate a valid cursor position from data
    data = check_cursor(data)

    # Move the cursor
    screen.move(data["cursor_y"], data["cursor_x"])

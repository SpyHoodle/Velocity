from modes import normal, insert, command


def activate(stdscr, data):
    if data["mode"] == "normal":
        data["mode_color"] = 6
        data = normal.activate(stdscr, data)

    elif data["mode"] == "insert":
        data["mode_color"] = 12
        data = insert.activate(stdscr, data)

    elif data["mode"] == "command":
        data["mode_color"] = 6
        data = command.activate(stdscr, data)

    return data

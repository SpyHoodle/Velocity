from modes import normal, insert, command


def activate(screen, data):
    if data["mode"] == "normal":
        data["mode_color"] = 6
        data = normal.activate(screen, data)

    elif data["mode"] == "insert":
        data["mode_color"] = 12
        data = insert.activate(screen, data)

    elif data["mode"] == "command":
        data["mode_color"] = 6
        data = command.activate(screen, data)

    return data

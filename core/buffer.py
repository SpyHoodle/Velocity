import curses


def write_buffer(screen, data):
    for index, line in enumerate(data["buffer_list"][data["visible_y"]:]):
        if index < data["height"] - 2:
            str_line = "".join(line)
            # [data["visible_x"]:1:data["width"] - data["visible_x"]]
            screen.addstr(index, len(data["info_bar"][0]), str_line + (" " * (len(line) - 1)), curses.color_pair(1))

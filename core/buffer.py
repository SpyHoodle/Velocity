import curses


def write_buffer(stdscr, data):
    count = 0
    for line in data["buffer_list"]:
        str_line = "".join(line)
        stdscr.addstr(count, len(data["info_bar"][0]), str_line + (" " * (len(line) - 1)), curses.color_pair(1))
        count += 1

import curses


def init_colors():
    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE,    curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK,    curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_RED,      curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLACK,    curses.COLOR_RED)
    curses.init_pair(5, curses.COLOR_GREEN,    curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_BLACK,    curses.COLOR_GREEN)
    curses.init_pair(7, curses.COLOR_YELLOW,   curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_BLACK,    curses.COLOR_YELLOW)
    curses.init_pair(9, curses.COLOR_CYAN,     curses.COLOR_BLACK)
    curses.init_pair(10, curses.COLOR_BLACK,   curses.COLOR_CYAN)
    curses.init_pair(11, curses.COLOR_BLUE,    curses.COLOR_BLACK)
    curses.init_pair(12, curses.COLOR_BLACK,   curses.COLOR_BLUE)
    curses.init_pair(13, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(14, curses.COLOR_BLACK,   curses.COLOR_MAGENTA)

import curses


class Codes:
    # Color codes
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    yellow = '\033[93m'
    cyan = '\033[96m'
    magenta = '\033[95m'
    white = '\033[97m'
    selected_white = '\033[47m'
    selected_green = '\033[42m'
    strike = '\033[9m'
    italic = '\033[3m'
    end = '\033[0m'


def init_colors():
    # Activate color support
    curses.start_color()

    # Foreground: WHITE, Background: BLACK
    curses.init_pair(1, curses.COLOR_WHITE,    curses.COLOR_BLACK)
    # Foreground: BLACK, Background: WHITE
    curses.init_pair(2, curses.COLOR_BLACK,    curses.COLOR_WHITE)
    # Foreground: RED, Background: BLACK
    curses.init_pair(3, curses.COLOR_RED,      curses.COLOR_BLACK)
    # Foreground: BLACK, Background: RED
    curses.init_pair(4, curses.COLOR_BLACK,    curses.COLOR_RED)
    # Foreground: GREEN, Background: BLACK
    curses.init_pair(5, curses.COLOR_GREEN,    curses.COLOR_BLACK)
    # Foreground: BLACK, Background: GREEN
    curses.init_pair(6, curses.COLOR_BLACK,    curses.COLOR_GREEN)
    # Foreground: YELLOW, Background: BLACK
    curses.init_pair(7, curses.COLOR_YELLOW,   curses.COLOR_BLACK)
    # Foreground: BLACK, Background: YELLOW
    curses.init_pair(8, curses.COLOR_BLACK,    curses.COLOR_YELLOW)
    # Foreground: CYAN, Background: BLACK
    curses.init_pair(9, curses.COLOR_CYAN,     curses.COLOR_BLACK)
    # Foreground: BLACK, Background: CYAN
    curses.init_pair(10, curses.COLOR_BLACK,   curses.COLOR_CYAN)
    # Foreground: BLUE, Background: BLACK
    curses.init_pair(11, curses.COLOR_BLUE,    curses.COLOR_BLACK)
    # Foreground: BLACK, Background: BLUE
    curses.init_pair(12, curses.COLOR_BLACK,   curses.COLOR_BLUE)
    # Foreground: MAGENTA, Background: BLACK
    curses.init_pair(13, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    # Foreground: BLACK, Background: MAGENTA
    curses.init_pair(14, curses.COLOR_BLACK,   curses.COLOR_MAGENTA)

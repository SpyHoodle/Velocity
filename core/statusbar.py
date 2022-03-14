import curses


def refresh(stdscr, height, width, mode, colors=None, theme="inverted", icon="λ", file="[No Name]"):
    if colors is None:
        colors = [8, 6, 14, 2]

    if theme == "inverted":
        # Add spaces on either end
        icon = f" {icon} "
        mode = f" {mode} "
        file = f" {file} "

    else:
        # Subtract one from all colours
        for index, color in enumerate(colors):
            colors[index] -= 1

        # Add spaces before each part
        icon = f" {icon}"
        mode = f" {mode}"
        file = f" {file}"

    # Render icon
    stdscr.addstr(height - 2, 0, icon, curses.color_pair(colors[0]) | curses.A_BOLD)

    # Render mode
    stdscr.addstr(height - 2, len(icon), mode, curses.color_pair(colors[1]) | curses.A_BOLD)

    # Render file name
    stdscr.addstr(height - 2, len(icon) + len(mode), file, curses.color_pair(colors[2]) | curses.A_BOLD)

    # Rest of the bar
    stdscr.addstr(height - 2, len(icon) + len(mode) + len(file), " " * (width - (len(icon) + len(mode) + len(file))),
                  curses.color_pair(colors[3]))

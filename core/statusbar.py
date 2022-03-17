import curses


def themes(data):
    if data["statusbar_theme"] == "bare":
        # The theme colors
        colors = (7, data["mode_color"] - 1, 13, 1)

        # Add spaces before each part
        icon = f" {data['icon']}"
        mode = f" {data['mode'].upper()}"
        file = f" {data['buffer_name']}"

    else:
        # The theme colors
        colors = (8, data["mode_color"], 14, 2)

        # Add spaces on either end
        icon = f" {data['icon']} "
        mode = f" {data['mode'].upper()} "
        file = f" {data['buffer_name']} "

    return colors, icon, mode, file


def refresh(screen, data):
    # Calculate the theme
    colors, icon, mode, file = themes(data)

    # Render icon
    screen.addstr(data["height"] - 2, 0, icon,
                  curses.color_pair(colors[0]) | curses.A_BOLD)

    # Render mode
    screen.addstr(data["height"] - 2, len(icon), mode,
                  curses.color_pair(colors[1]) | curses.A_BOLD)

    # Render file name
    screen.addstr(data["height"] - 2, len(icon) + len(mode), file,
                  curses.color_pair(colors[2]) | curses.A_BOLD)

    # Rest of the bar
    screen.addstr(data["height"] - 2, len(icon) + len(mode) + len(file),
                  " " * (data["width"] - (len(icon) + len(mode) + len(file))),
                  curses.color_pair(colors[3]))

import curses


def start_screen(screen):
    # Get window height and width
    height, width = screen.getmaxyx()

    # Startup text
    title = "λ Lambda"
    subtext = [
        "Next generation hackable text editor for nerds",
        "",
        "Type :h to open the README.md document",
        "Type :o <file> to open a file and edit",
        "Type :q or <C-c> to quit lambda.py"
    ]

    # Centering calculations
    start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
    start_y = int((height // 2) - 2)

    # Rendering title
    screen.addstr(start_y, start_x_title, title, curses.color_pair(7) | curses.A_BOLD)

    # Print the subtext
    for text in subtext:
        start_y += 1
        start_x = int((width // 2) - (len(text) // 2) - len(text) % 2)
        screen.addstr(start_y, start_x, text)

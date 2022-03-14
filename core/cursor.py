def cursor_mode(mode):
    if mode == "block":
        print("\033[2 q")
    elif mode == "line":
        print("\033[6 q")
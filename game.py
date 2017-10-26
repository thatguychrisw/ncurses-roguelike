import curses


def game(stdscr):
    # Hide the cursor
    curses.curs_set(0)

    # define the current key, and player coordinates
    key = 0
    x = 0
    y = 0

    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_WHITE, -1)

    height, width = stdscr.getmaxyx()

    while key != ord('q'):

        stdscr.clear()

        # draw map
        for r in range(0, height - 1):
            for c in range(0, width):
                stdscr.addstr(r, c, ".", curses.color_pair(1))

        if key == curses.KEY_UP:
            y = y - 1
        if key == curses.KEY_RIGHT:
            x = x + 1
        if key == curses.KEY_DOWN:
            y = y + 1
        if key == curses.KEY_LEFT:
            x = x - 1

        x = max(0, x)
        x = min(width - 1, x)

        y = max(0, y)
        y = min(height - 2, y)

        stdscr.addstr(y, x, "@", curses.color_pair(1))

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height - 1, 0, "y: " + str(y) + ", x: " + str(x), curses.color_pair(1))
        stdscr.attroff(curses.color_pair(3))

        stdscr.refresh()

        key = stdscr.getch()
    pass


def main():
    curses.wrapper(game)


if __name__ == '__main__':
    main()

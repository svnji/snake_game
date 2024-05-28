import curses
import random

def main(screen):
    curses.curs_set(0)
    screen_height, screen_width = screen.getmaxyx()
    window = curses.newwin(screen_height, screen_width, 0, 0)
    window.keypad(True)
    window.timeout(125)
    
    snk_x = screen_width // 4
    snk_y = screen_height // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]
    food = [screen_height // 2, screen_width // 2]
    window.addch(food[0], food[1], curses.ACS_PI)
    key = curses.KEY_RIGHT

    while True:
        next_key = window.getch()
        key = key if next_key == -1 else next_key
        
        new_head = [snake[0][0], snake[0][1]]
        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1

        if (
            new_head[0] in [0, screen_height] or
            new_head[1] in [0, screen_width] or
            new_head in snake
        ):
            curses.endwin()
            quit()
        
        snake.insert(0, new_head)

        if snake[0] == food:
            food = None
            while food is None:
                new_food = [
                    random.randint(1, screen_height - 2),
                    random.randint(1, screen_width - 2)
                ]
                food = new_food if new_food not in snake else None
            window.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            window.addch(tail[0], tail[1], ' ')

        window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

if __name__ == "__main__":
    curses.wrapper(main)

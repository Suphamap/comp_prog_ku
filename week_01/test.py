from turtle import *

STEPS = 40
PIXEL = 40


def draw_pixel(col):
    # Set each pixel to have a unique color
    fillcolor(col)

    # Create a pixel
    begin_fill()
    for i in range(4):
        forward(PIXEL)
        left(90)
    end_fill()

    print(position())


def move_up():
    current_pos = position()
    new_pos = Vec2D(current_pos[0], current_pos[1] + STEPS)
    teleport(new_pos[0], new_pos[1])

def draw_move_up(col):
    move_up()
    draw_pixel(col)

def move_down():
    current_pos = position()
    new_pos = Vec2D(current_pos[0], current_pos[1] - STEPS)
    teleport(new_pos[0], new_pos[1])

def draw_move_down(col):
    move_down()
    draw_pixel(col)


def move_left():
    current_pos = position()
    new_pos = Vec2D(current_pos[0] - STEPS, current_pos[1])
    teleport(new_pos[0], new_pos[1])

def draw_move_left(col):
    move_left()
    draw_pixel(col)

def move_right():
    current_pos = position()
    new_pos = Vec2D(current_pos[0] + STEPS, current_pos[1])
    teleport(new_pos[0], new_pos[1])

def draw_move_right(col):
    move_right()
    draw_pixel(col)

def draw_diagonal(count, col):
    for i in range(count):
        print(position())
        draw_pixel(col)
        move_right()
        move_up()


def draw_diagonal_color(count, first_col, second_color):
    for i in range(count):
        print(position())
        draw_pixel(first_col)
        move_right()
        move_up()
        draw_pixel(second_color)
        move_right()
        move_up()


def main():
    # Origin point
    teleport(-6 * PIXEL, -7 * PIXEL)

    # Draw an axe handle
    dark_brown = "#281E0C"
    medium_brown = "#584119"
    light_brown = "#896727"
    tan_brown = "#684E1E"

    draw_pixel(dark_brown)
    move_up()
    draw_diagonal(8, medium_brown)

    teleport(-5 * PIXEL, -6 * PIXEL)
    draw_diagonal_color(3, light_brown, tan_brown)
    draw_diagonal(1, tan_brown)

    teleport(-5 * PIXEL, -7 * PIXEL)
    draw_diagonal(8, dark_brown)

    # Draw an axe head for the border section
    dark_blue = "#18172D"
    jungle_green = "#0D3F36"

    teleport(0 * PIXEL, 1 * PIXEL)
    draw_pixel(dark_blue)
    draw_move_left(dark_blue)
    move_up()
    draw_move_left(jungle_green)
    draw_pixel(dark_blue)
    draw_move_up(jungle_green)
    draw_diagonal(4, jungle_green)
    teleport(1*PIXEL, 6*PIXEL)
    draw_move_right(jungle_green)
    move_right()
    for _ in range(2):
        draw_move_down(jungle_green)
    draw_move_down(tan_brown)
    draw_move_right(medium_brown)
    draw_move_down(dark_brown)
    move_right()
    for _ in range(2):
        draw_move_down(dark_blue)
    move_down()
    for _ in range(2):
        draw_move_left(dark_blue)

    # Color in the axe head
    cyan = "#32EBCB"
    teal = "#2BC7AC"
    dark_cyan = "#26B29A"
    dark_teal = "#1E8A77"
    teleport(1 * PIXEL, 2*PIXEL)
    draw_pixel(dark_cyan)
    draw_move_left(teal)
    draw_move_left(cyan)
    move_up()
    draw_diagonal(3, cyan)
    teleport(2 * PIXEL, 5 * PIXEL)
    draw_pixel(cyan)
    draw_move_down(teal)
    draw_move_down(dark_cyan)
    draw_move_down(dark_teal)
    draw_move_right(teal)
    draw_move_down(dark_teal)
    draw_move_right(cyan)
    draw_move_down(cyan)
    draw_move_left(cyan)
    teleport(2 * PIXEL, 1 * PIXEL)
    draw_pixel(teal)
    teleport(0 * PIXEL, 3*PIXEL)
    draw_pixel(dark_cyan)
    draw_move_right(dark_cyan)
    draw_move_up(dark_cyan)
    
    
main()
done()
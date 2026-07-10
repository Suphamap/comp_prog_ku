import turtle


def move_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_polygon(points, fill_color, outline_color="black"):
    turtle.color(outline_color, fill_color)
    turtle.penup()
    turtle.goto(points[0])
    turtle.pendown()
    turtle.begin_fill()
    for point in points[1:]:
        turtle.goto(point)
    turtle.goto(points[0])
    turtle.end_fill()


def draw_rectangle(x, y, width, height, fill_color, outline_color="black"):
    points = [
        (x, y),
        (x + width, y),
        (x + width, y + height),
        (x, y + height),
    ]
    draw_polygon(points, fill_color, outline_color)


def draw_sword():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.pensize(3)

    # Blade
    blade_points = [
        (-20, -160),
        (20, -160),
        (40, 80),
        (0, 190),
        (-40, 80),
    ]
    draw_polygon(blade_points, "#cfd8dc", "#546e7a")

    # Central ridge
    move_to(0, -140)
    turtle.color("#90a4ae")
    turtle.pensize(5)
    turtle.goto(0, 165)

    # Guard
    draw_rectangle(-90, -190, 180, 28, "#8d6e63", "#4e342e")
    draw_rectangle(-60, -215, 120, 20, "#5d4037", "#3e2723")

    # Handle
    draw_rectangle(-16, -290, 32, 95, "#6d4c41", "#3e2723")

    # Grip wrap
    turtle.pensize(2)
    turtle.color("#1b1b1b")
    for y in range(-280, -210, 14):
        move_to(-16, y)
        turtle.goto(16, y + 8)

    # Pommel
    draw_polygon([(-30, -305), (30, -305), (20, -340), (-20, -340)], "#757575", "#424242")
    draw_polygon([(-14, -340), (14, -340), (0, -365)], "#9e9e9e", "#424242")

    turtle.penup()
    turtle.goto(0, 0)


def main():
    screen = turtle.Screen()
    screen.title("Sword")
    screen.bgcolor("#f5f5f5")
    screen.setup(width=800, height=800)
    draw_sword()
    turtle.done()


if __name__ == "__main__":
    main()

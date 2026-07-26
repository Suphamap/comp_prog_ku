LAB = "turtlelab8.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab8 import turtle,radar,check

# Put your turtle movement commands here
def reset_dir(x):
    angle = turtle.heading
    turtle.right(angle)
    turtle.left(x)

radar_dir = radar.ball_direction()
while radar_dir != "x":
    radar_dir = radar.ball_direction()
    distance = 50
    if radar_dir == "n":
        reset_dir(90)
        turtle.forward(distance)
    elif radar_dir == "e":
        reset_dir(0)
        turtle.forward(distance)
    elif radar_dir == "w":
        reset_dir(180)
        turtle.forward(distance)
    elif radar_dir == "s":
        reset_dir(270)
        turtle.forward(distance)
    elif radar_dir == "ne":
        reset_dir(45)
        turtle.forward(distance)
    elif radar_dir == "nw":
        reset_dir(135)
        turtle.forward(distance)
    elif radar_dir == "sw":
        reset_dir(225)
        turtle.forward(distance)
    elif radar_dir == "se":
        reset_dir(315)
        turtle.forward(distance)
check()

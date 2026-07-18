LAB = "turtlelab6.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.14",LAB)

from turtlelab6 import turtle,home,luigi,mozart,check
from math import degrees, atan2

# Put your turtle movement commands here
def distance(x, y, x_c, y_c):
    dx, dy = x_c - x, y_c - y
    distance = (dx**2 + dy**2)**0.5
    return distance

def is_fastest():
    dn_1 = distance(mozart.x, mozart.y, turtle.x, turtle.y)
    dn_1 += distance(luigi.x, luigi.y, home.x, home.y)
    dn_2 = distance(luigi.x, luigi.y, turtle.x, turtle.y)
    dn_2 += distance(mozart.x, mozart.y, home.x, home.y)
    if dn_1 < dn_2:
        return mozart.x, mozart.y, luigi.x, luigi.y
    else:
        return luigi.x, luigi.y, mozart.x, mozart.y

def heading_to(x, y):
    turtle.right(turtle.heading)
    dy = y - turtle.y
    dx = x - turtle.x
    turtle.left(degrees(atan2(dy, dx)))

def moveto(x, y):
    """Move Turtle to location (x,y)"""
    dx, dy = turtle.x - x, turtle.y - y
    distance = (dx**2 + dy**2)**0.5
    heading_to(x, y)
    turtle.forward(distance)

# main program
x_1, y_1, x_2, y_2 = is_fastest()
moveto(x_1, y_1)
moveto(x_2, y_2)
moveto(home.x, home.y)

turtle.done()
check()
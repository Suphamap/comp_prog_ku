LAB = "turtlelab5x.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab5x import turtle,mickey,raph,leo,donnie,check
from math import degrees, atan2

def heading_to(x, y):
    turtle.right(turtle.heading)
    y = y - turtle.y
    x = x - turtle.x
    print(x, y)
    turtle.left(degrees(atan2(y, x)))

def moveto(x,y, name):
    """Move Turtle to location (x,y)"""
    tr_hx, tr_hy = turtle.x - x, turtle.y - y
    distance = (tr_hx**2 + tr_hy**2)**0.5
    heading_to(x, y)
    turtle.forward(distance)

# main program
moveto(mickey.x, mickey.y, mickey)
moveto(raph.x, raph.y, raph)
moveto(leo.x, leo.y, leo)
moveto(donnie.x, donnie.y, donnie)

turtle.done()
check()
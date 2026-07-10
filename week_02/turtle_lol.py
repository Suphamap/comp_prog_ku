LAB = "turtlelab2x.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab2x import turtle,home,shop,check
from math import *

# Put your turtle movement commands here
def move(distance, angle):
    turtle.left(angle)
    turtle.forward(distance)
print(shop.x)

distance_shop = sqrt((shop.x**2) + (shop.y**2))
distance_home = sqrt((home.x - shop.x)**2 + (home.y - shop.y)**2)
angle_shop = degrees(atan(shop.y/shop.x))
angle_home = degrees(atan((home.y-shop.y)/(home.x-shop.x)))

move(distance_shop, angle_shop)
turtle.right(angle_shop)
move(distance_home, angle_home)

print(distance_shop, angle_home)
turtle.done()
check()
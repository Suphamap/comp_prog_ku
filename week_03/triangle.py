import math

def read_point(msg):
    print(f"Point {msg}")
    x = float(input("x: "))
    y = float(input("y: "))
    return x, y

def distance(x1, x2, y1, y2):
    dist = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    return dist

x1,y1 = read_point("A")
print()
x2,y2 = read_point("B")

print()
x3,y3 = read_point("C")

print()
line_AB = distance(x1, x2, y1, y2)
line_BC = distance(x2, x3, y2, y3)

line_AC = distance(x1, x3, y1, y3)

perimeter = line_AB + line_BC + line_AC
print(f"Perimeter = {perimeter:.2f}")
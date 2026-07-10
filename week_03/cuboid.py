def compute_rectangle_area(first_side,second_side):
    return first_side*second_side

def compute_surface_area(width,length,height):
    first_side = compute_rectangle_area(width, length)
    second_side = compute_rectangle_area(width, height)
    third_side = compute_rectangle_area(length, height)
    return (first_side+second_side+third_side)*2

def compute_volume(width,length,height):
    return width*length*height

# main program
width = float(input("Enter width: "))
length = float(input("Enter length: "))
height = float(input("Enter height: "))

print(f"For [{width:.2f} x {length:.2f} x {height:.2f}] cuboid:")
print(f"Surface area = {compute_surface_area(width, length, height):.3f}")
print(f"Volume = {compute_volume(width, length, height):.3f}")

width, length, height = width*2, length*2, height*2
print()
print("After doubling each side,")
print(f"For [{width:.2f} x {length:.2f} x {height:.2f}] cuboid:")
print(f"Surface area = {compute_surface_area(width, length, height):.3f}")
print(f"Volume = {compute_volume(width, length, height):.3f}")

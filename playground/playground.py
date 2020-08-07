# TODO: it's a playground, let's write some code (no unit tests to run here)
from math import pi

# radius = 5
# perimeter = pi * 2 * radius
# area = (pi) * (radius ** 2)

# print(f"The radius is set to {radius}")
# print(f"Perimeter of the circle is {round(perimeter, 1)}")
# print(f"The area of the disk is {round(area,1)}")

def circle_math(radius):
    perimeter = pi * 2 * radius
    area = (pi) * (radius ** 2)
    return [ perimeter, area]
    
values = circle_math(5)
print(f"Radius=5 => Perimeter={round(values[0], 1)}, Area={round(values[1], 1)}")

values = circle_math(6)
print(f"Radius=6 => Perimeter={round(values[0], 1)}, Area={round(values[1], 1)}")


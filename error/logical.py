# Logical error
import math


print("This is a logical error example.")

def calculate_area(radius):
    # This is a logical error because the formula for the area of a circle is incorrect
    area = math.pi * radius * radius * radius  # Should be math.pi * radius * radius
    return area

# This will not raise an error, but it will give an incorrect result
radius = 5
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is: {area}")
import math
def calculate_circle_area(radius):
  area = math.pi * radius**2  # or math.pow(radius, 2) 
  return area
radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is {area}")
radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is {area}")

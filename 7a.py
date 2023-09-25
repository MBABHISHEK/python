class Shape:
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

def calculate_area(object_received):
    return object_received.area()

triangle = Triangle(6, 8)
circle = Circle(5)
rectangle = Rectangle(4, 10)
print("Area of Triangle:", calculate_area(triangle))
print("Area of Circle:", calculate_area(circle))
print("Area of Rectangle:", calculate_area(rectangle))

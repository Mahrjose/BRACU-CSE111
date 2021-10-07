import math


class Circle:
    def __init__(self, radius=None):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius
        return self.radius

    def area(self):
        self.area = (math.pi) * self.radius * self.radius
        return self.area

    def __add__(self, other):
        return Circle(self.radius + other.radius)


c1 = Circle(4)
print("First circle radius:", c1.getRadius())
print("First circle area:", c1.area())

c2 = Circle(5)
print("Second circle radius:", c2.getRadius())
print("Second circle area:", c2.area())

c3 = c1 + c2
print("Third circle radius:", c3.getRadius())
print("Third circle area:", c3.area())

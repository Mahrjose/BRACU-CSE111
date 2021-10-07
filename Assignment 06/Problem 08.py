from math import pi


class Cylinder:

    radius = 5
    height = 18

    def __init__(self, radius, height):

        print(f"Default radius = {Cylinder.radius} and height = {Cylinder.height}.")

        Cylinder.radius = radius
        Cylinder.height = height

        print(f"Updated: radius = {Cylinder.radius} and height = {Cylinder.height}.")

    @classmethod
    def swap(cls, height, radius):
        return cls(radius, height)

    @classmethod
    def changeFormat(cls, info_str):
        radius, height = info_str.split("-")
        radius = float(radius)
        height = float(height)
        return cls(radius, height)

    @staticmethod
    def area(radius, height):
        area = 2 * pi * (radius ** 2) + 2 * pi * radius * height
        print(f"Area: {area}")

    @staticmethod
    def volume(radius, height):
        volume = pi * (radius ** 2) * height
        print(f"Volume: {volume}")


c1 = Cylinder(0, 0)
Cylinder.area(c1.radius, c1.height)
Cylinder.volume(c1.radius, c1.height)
print("===============================")
c2 = Cylinder.swap(8, 3)
c2.area(c2.radius, c2.height)
c2.volume(c2.radius, c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius, c3.height)
c3.volume(c3.radius, c3.height)
print("===============================")
Cylinder(0.3, 5.56).area(Cylinder.radius, Cylinder.height)
print("===============================")
Cylinder(3, 5).volume(Cylinder.radius, Cylinder.height)

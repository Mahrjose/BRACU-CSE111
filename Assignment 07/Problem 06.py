class Shape:
    def __init__(self, name="Default", height=0, base=0):
        self.area = 0
        self.name = name
        self.height = height
        self.base = base

    def get_height_base(self):
        return "Height: " + str(self.height) + ", Base: " + str(self.base)


class triangle(Shape):
    def calcArea(self):
        self.area = (self.height * self.base) / 2

    def printDetail(self):

        return (
            f"Shape name: {self.name}\n"
            + super().get_height_base()
            + f"\nArea: {self.area}"
        )


class trapezoid(Shape):
    def __init__(self, name, height, base, side_A):
        super().__init__(name, height, base)
        self.side_A = side_A

    def calcArea(self):
        self.area = ((self.base + self.side_A) / 2) * self.height

    def printDetail(self):
        return (
            f"Shape name: {self.name}\n"
            + super().get_height_base()
            + f", Side_A: {self.side_A}"
            + f"\nArea: {self.area}"
        )


tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print("--------------------------")
tri = triangle("Triangle", 10, 5)
tri.calcArea()
print(tri.printDetail())
print("---------------------------")
trap = trapezoid("Trapezoid", 10, 6, 4)
trap.calcArea()
print(trap.printDetail())

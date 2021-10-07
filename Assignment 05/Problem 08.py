# task-8
class Coordinates:
    def __init__(self, x_axis, y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis

    def detail(self):
        return (self.x_axis, self.y_axis)

    def __sub__(self, other):
        a = self.x_axis - other.x_axis
        b = self.y_axis - other.y_axis
        return Coordinates(a, b)

    def __mul__(self, other):
        c = self.x_axis * other.x_axis
        d = self.y_axis * other.y_axis
        return Coordinates(c, d)

    def __eq__(self, other):
        if self.x_axis == other.x_axis:
            return "The calculated coordinates are the same."
        else:
            return "The calculated coordinates are NOT the same."


p1 = Coordinates(int(input()), int(input()))
p2 = Coordinates(int(input()), int(input()))
p4 = p1 - p2
print(p4.detail())
p5 = p1 * p2
print(p5.detail())
point_check = p4 == p5
print(point_check)

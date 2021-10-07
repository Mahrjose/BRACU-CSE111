class Vehicle:
    def __init__(self):
        self.x_axis = 0
        self.y_axis = 0

    def moveUp(self):
        self.y_axis += 1

    def moveDown(self):
        self.y_axis -= 1

    def moveRight(self):
        self.x_axis += 1

    def moveLeft(self):
        self.x_axis -= 1

    def print_position(self):
        print(f"({self.x_axis}, {self.y_axis})")


car = Vehicle()
car.print_position()
car.moveUp()
car.print_position()
car.moveLeft()
car.print_position()
car.moveDown()
car.print_position()
car.moveRight()

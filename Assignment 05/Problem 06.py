class Triangle:
    def __init__(self, base=None, height=None):
        self.__base = base
        self.__height = height

    def getBase(self):
        return self.__base

    def setBase(self, base):
        self.__base = base
        return self.__base

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height
        return self.__height

    def area(self):
        self.area = 0.5 * self.__base * self.__height
        return self.area

    def __sub__(self, other):
        self.new_base = self.__base - other.__base
        self.new_height = self.__height - other.__height
        return Triangle(self.new_base, self.new_height)


t1 = Triangle(10, 5)
print("First Triangle Base:", t1.getBase())
print("First Triangle Height:", t1.getHeight())
print("First Triangle area:", t1.area())

t2 = Triangle(5, 3)
print("Second Triangle Base:", t2.getBase())
print("Second Triangle Height:", t2.getHeight())
print("Second Triangle area:", t2.area())

t3 = t1 - t2
print("Third Triangle Base:", t3.getBase())
print("Third Triangle Height:", t3.getHeight())
print("Third Triangle area:", t3.area())

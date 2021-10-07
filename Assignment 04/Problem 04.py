class Cat:
    def __init__(self, color="White", activity="sitting"):
        self.color = color
        self.activity = activity

    def printCat(self):
        print(f"{self.color} cat is {self.activity}")

    def changeColor(self, new_color):
        self.color = new_color


c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()

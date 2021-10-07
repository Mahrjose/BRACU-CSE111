class Color:
    def __init__(self, color):
        self.clr = color

    def __add__(self, other):
        self.clr = self.clr + other.clr

        if self.clr == "redyellow" or self.clr == "yellowred":
            self.clr = "Orange"
        elif self.clr == "redblue" or self.clr == "bluered":
            self.clr = "Violet"
        elif self.clr == "yellowblue" or self.clr == "blueyellow":
            self.clr = "Green"

        return Color(self.clr)


C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.clr)

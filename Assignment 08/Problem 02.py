class RealNumber:
    def __init__(self, number=0):
        self.number = number

    def __add__(self, anotherRealNumber):
        return self.number + anotherRealNumber.number

    def __sub__(self, anotherRealNumber):
        return self.number - anotherRealNumber.number

    def __str__(self):
        return str(self.number)


class ComplexNumber(RealNumber):
    def __init__(self, real, imaginary):

        if isinstance(real, int):
            super().__init__(real)
            self.imaginary = imaginary
        else:
            super().__init__(real.number)
            self.imaginary = imaginary

    def __add__(self, other):

        real_num = (self.number) + (other.number)
        imaginary_num = (self.imaginary) + other.imaginary

        return ComplexNumber(real_num, imaginary_num)

    def __sub__(self, other):

        real_num = (self.number) - (other.number)
        imaginary_num = (self.imaginary) - other.imaginary

        return ComplexNumber(real_num, imaginary_num)

    def __str__(self):
        if self.imaginary < 0:
            return f"{str(self.number) + str(self.imaginary)}i"
        else:
            return f"{self.number} + {self.imaginary}i"


r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1 + r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1, 5)
print(cn2)
cn3 = cn1 + cn2
print(cn3)
cn4 = cn1 - cn2
print(cn4)

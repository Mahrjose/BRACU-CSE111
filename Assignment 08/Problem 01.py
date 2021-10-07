class RealNumber:
    def __init__(self, r=0):
        self.__realValue = r

    def getRealValue(self):
        return self.__realValue

    def setRealValue(self, r):
        self.__realValue = r

    def __str__(self):
        return "RealPart: " + str(self.getRealValue())


class ComplexNumber(RealNumber):
    def __init__(self, r=1, i=1):
        super().__init__(r)
        self.imaginary_Value = i

    def __str__(self):
        return f"RealPart: {str(float(self.getRealValue()))}\nImaginaryPart: {str(float(self.imaginary_Value))}"


cn1 = ComplexNumber()
print(cn1)
print("---------")
cn2 = ComplexNumber(5, 7)
print(cn2)

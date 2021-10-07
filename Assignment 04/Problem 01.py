class Calculator:
    def __init__(self, first_value, operator, second_value):
        print("Let's Calculate!")
        self.first_value = first_value
        self.operator = operator
        self.second_value = second_value

        print(f"Value 1: {self.first_value}")
        print(f"Operator: {self.operator}")
        print(f"Value 2: {self.second_value}")

        if self.operator == "+":
            Calculator.add(self)
        elif self.operator == "-":
            Calculator.subtract(self)
        elif self.operator == "*":
            Calculator.multiply(self)
        elif self.operator == "/":
            Calculator.divide(self)

    def add(self):
        print(f"Result : {self.first_value + self.second_value}")

    def subtract(self):
        print(f"Result : {self.first_value - self.second_value}")

    def multiply(self):
        print(f"Result : {self.first_value * self.second_value}")

    def divide(self):
        print(f"Result : {self.first_value / self.second_value}")


first_value = int(input())
operator = input()
second_value = int(input())

calc = Calculator(first_value, operator, second_value)

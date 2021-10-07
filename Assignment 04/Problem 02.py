class Customer:
    def __init__(self, name):
        self.name = name

    def greet(self, name=None):
        if name != None:
            print(f"Hello {name}!")
        else:
            print("Hello!")

    def purchase(self, *item):
        print(f"{self.name}, you purchased {len(item)} items(s):")
        for i in item:
            print(i)


customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")

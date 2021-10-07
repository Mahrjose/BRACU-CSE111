class ParcelKoro:
    def __init__(self, name=None, product_weight=None) -> None:
        self.name = name
        self.product_weight = product_weight
        if self.product_weight == None:
            self.product_weight = 0

    def calculateFee(self, location=None):
        self.location = location

        if location == None:
            location_charge = 50
        else:
            location_charge = 100

        if self.product_weight == 0:
            self.total_fee = 0
        else:
            self.total_fee = (self.product_weight * 20) + location_charge

    def printDetails(self):
        if self.name == None:
            self.name = "No name set"

        print(f"Customer Name: {self.name}")
        print(f"Product Weight: {self.product_weight}")
        print(f"Total fee: {self.total_fee}")


print("**********************")
p1 = ParcelKoro()
p1.calculateFee()
p1.printDetails()
print("**********************")
p2 = ParcelKoro("Bob The Builder")
p2.calculateFee()
p2.printDetails()
print("----------------------------")
p2.product_weight = 15
p2.calculateFee()
p2.printDetails()
print("**********************")
p3 = ParcelKoro("Dora The Explorer", 10)
p3.calculateFee("Dhanmondi")
p3.printDetails()

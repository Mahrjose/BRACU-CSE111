class SultansDine:

    total_branch = 0
    total_sell = 0
    branch_info = []

    def __init__(self, branch):
        self.name = branch
        SultansDine.total_branch += 1

    def sellQuantity(self, quantity):

        if quantity < 10:
            self.branch_sell = quantity * 300
        elif quantity < 20:
            self.branch_sell = quantity * 350
        else:
            self.branch_sell = quantity * 400

        SultansDine.total_sell += self.branch_sell

    def branchInformation(self):
        print(f"Branch Name: {self.name}")
        print(f"Branch Sell: {self.branch_sell}")

        SultansDine.branch_info.append(self.name)
        SultansDine.branch_info.append(self.branch_sell)

    @classmethod
    def details(cls):
        print(f"Total Number of branch(s): {cls.total_branch}")
        print(f"Total Sell: {cls.total_sell}")

        for index in range(0, len(SultansDine.branch_info), 2):
            print(
                f"Branch Name: {SultansDine.branch_info[index]}, Branch Sell: {SultansDine.branch_info[index + 1]} Taka"
            )
            print(
                f"Branch consists of total sell's: {(SultansDine.branch_info[index + 1] / SultansDine.total_sell) * 100:.2f}%"
            )


SultansDine.details()
print("########################")
dhanmodi = SultansDine("Dhanmondi")
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print("-----------------------------------------")
SultansDine.details()
print("========================")
baily_road = SultansDine("Baily Road")
baily_road.sellQuantity(15)
baily_road.branchInformation()
print("-----------------------------------------")
SultansDine.details()
print("========================")
gulshan = SultansDine("Gulshan")
gulshan.sellQuantity(9)
gulshan.branchInformation()
print("-----------------------------------------")
SultansDine.details()

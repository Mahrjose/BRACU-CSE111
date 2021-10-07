class Account:
    def __init__(self, name=None, balance=None):
        self.name = name
        self.balance = balance

        if self.name == None:
            self.name = "Default Account"

        if self.balance == None:
            self.balance = 0.0

    def withdraw(self, amount):
        var = self.balance - amount
        if var <= 3070.0:
            print(
                "Sorry, Withdraw unsuccessful! The account balance after deducting withdraw amount is equal to or less than minimum."
            )
        else:
            print(f"Withdraw successful! New balance is: {var}")

    def details(self):
        return f"{self.name}\n{self.balance:.1f}"


a1 = Account()
print(a1.details())
print("------------------------")
a1.name = "Oliver"
a1.balance = 10000.0
print(a1.details())
print("------------------------")
a2 = Account("Liam")
print(a2.details())
print("------------------------")
a3 = Account("Noah", 400)
print(a3.details())
print("------------------------")
a1.withdraw(6930)
print("------------------------")
a2.withdraw(600)
print("------------------------")
a1.withdraw(6929)

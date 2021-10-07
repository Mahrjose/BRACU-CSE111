class Author:
    def __init__(self, name=None, *books):
        self.name = name
        if name == None:
            self.name = "Default"

        booklist = ""
        if len(books) > 0:
            for i in books:
                booklist += i + "\n"
            self.books = booklist

    def changeName(self, new_name):
        self.name = new_name

    def addBooks(self, *books):
        booklist = ""
        for i in books:
            booklist += i + "\n"

        self.books = booklist

    def printDetails(self):
        print(f"Author Name: {self.name}")
        print("------------")
        print(f"List of Books:")
        print(self.books)


auth1 = Author("Humayun Ahmed")
auth1.addBooks("Deyal", "Megher Opor Bari")
auth1.printDetails()
print("===================")
auth2 = Author()
print(auth2.name)
auth2.changeName("Mario Puzo")
auth2.addBooks("The Godfather", "Omerta", "The Sicilian")
print("===================")
auth2.printDetails()
print("===================")
auth3 = Author("Paolo Coelho", "The Alchemist", "The Fifth Mountain")
auth3.printDetails()

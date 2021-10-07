class Travel:

    count = 0

    def __init__(self, source, destination, time=1):
        self.source = source
        self.destination = destination
        self.time = time
        Travel.count += 1

    def set_source(self, source):
        self.source = source

    def set_destination(self, destination):
        self.destination = destination

    def set_time(self, time):
        self.time = time

    def display_travel_info(self):
        info_str = f"Source: {self.source}\nDestination: {self.destination}\nFlight Time: {self.time}:00"
        return info_str


print("No. of Traveller =", Travel.count)
print("=======================")
t1 = Travel("Dhaka", "India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur", "Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka", "New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka", "India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print("No. of Traveller =", Travel.count)

class House:
    area = "Munich"

    def __init__(self, street, number):
        self.street = street
        self.num = number


h1 = House("Offenbachstarsse", 123)
h2 = House("Offenbachstarsse", 145)
# area is found in the class dictionary
# so the value is the same between object instances as the h1.area and h2.area are pointing to area from class dictionary
print(h1.street + ',' + str(h1.num) + ',' + h1.area)
print(h2.street + ',' + str(h2.num)+ ',' + h2.area)
# area is found in the class dictionary for h1 but assignment of a new value to h2.area creates an entry in the local dictionary of the object
# so the value is not the same between object instances
h2.area = "Regensburg"
print(h1.street + ',' + str(h1.num) + ',' + h1.area)
print(h2.street + ',' + str(h2.num)+ ',' + h2.area)
# update using the class impacts only the entry in the class dictionary,
# therefore the h1.area shows the new update but h2.area is referring to the local dictionary entry for the instance
House.area = "Germany"
print(h1.street + ',' + str(h1.num) + ',' + h1.area)
print(h2.street + ',' + str(h2.num)+ ',' + h2.area)
# Project from Codecademy's Learn Python 3 course
# Create a system to keep a restaurant business organized

# Menu class holds menus which have a name, a dictionary of menu items
# which have the item name as their key and price as their value, a start time and an end time
# for when that menu is available.
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return self.name + " menu available from " + str(self.start_time) + " to " + str(self.end_time)

# Accepts a list of purchased items and returns the price by 
# looking them up in the dictionary
    def calculate_bill(self, purchased_items):
        price = 0
        for item in purchased_items:
            price += self.items[item]
        return price

# Franchise class which has an address and a list of menus available
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

# Outputs a list of available menus at any given time
    def available_menus(self, time):
        available = []
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                available.append(menu)
        return available

# Business class which has a business name and a list of its franchises
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

# Creating the first four menus
brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50,
                         'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 1100, 1600)

early_bird = Menu("Early Bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                                 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00, }, 1500, 1800)

dinner = Menu("Dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
                         'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00, }, 1700, 2300)

kids = Menu("Kids", {'chicken nuggets': 6.50,
                     'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 1100, 2100)

# Creating two franchises
flagship_store = Franchise("1232 West End Road", [
                           brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [
                            brunch, early_bird, dinner, kids])

# Creating the original business
basta = Business("Basta Fazoolin' with my Heart", [
                 flagship_store, new_installment])

# Creating the menu for a new business
arepas_menu = Menu("Arepas", {'arepa pabellon': 7.00, 'pernil arepa': 8.50,
                              'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 1000, 2000)

# Creating the new franchise for the new business
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# Creating the new business
arepas = Business("Take a' Arepa", [arepas_place])

# Tests
print(brunch)
print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
print(early_bird.calculate_bill(
    ["salumeria plate", "mushroom ravioli (vegan)"]))
print(flagship_store.available_menus(1700))
print(arepas.franchises[0].available_menus(1300))
from Menu import Pizza, Burger, Drinks, Menu
from Restuarant_sub import Restuarant
from Restuarant_Project import Chef, Customer, Server, Manager

def Main():
    menu = Menu()
    pizza_1 = Pizza("Shutki Pizza", 600, "Large", "vegitables varites with shutki")
    menu.add_menu_item('Pizza', pizza_1)
    pizza_2 = Pizza("Alur Pizza", 400, "Large", ['alu', 'oil', 'onion', 'vegitables', 'salad'])
    menu.add_menu_item('Pizza', pizza_2)
    pizza_3 = Pizza("Daal Pizza", 500, "Large", ['daal','oil'])
    menu.add_menu_item('Pizza', pizza_3)


    # Add Burger to the menu:
    burger_1 = Burger("Naga Burger", 1000, "Chicken", ["Bread", "Naga Chili"])
    menu.add_menu_item("Burger", burger_1)
    burger_2 = Burger("Mutton Burger", 1400, "Mutton", ['Bread', "Soses", 'salad', 'Mutton', "Haddii"])
    menu.add_menu_item("Burger", burger_2)


    # Add Drinks to the menu:
    coke = Drinks('Coke', 50, True)
    menu.add_menu_item("Drinks", coke)
    coffee = Drinks("Americano", 300, False)
    menu.add_menu_item("Drinks", coffee)


    # SHow Menu:
    menu.show_menu()

    restuarant = Restuarant("Sai Baba Restuarant",2000, menu)

    # Add Employees:
    manager = Manager("Kala Chan Manager", 5, "Kala@chan.com", 'Kalidaha', 15000, "Jan-1-2020", "Core")
    restuarant.add_employee('Manager', manager)

    chef = Chef("Rustom Baburchi", 5699, "Chupa@rus.com", "rustamnagar", 4000, "Feb-01-2020","Chef", "Everything")
    restuarant.add_employee("Chef", chef)

    server = Server("Lolu",4566789, "nai@.com", 'Restuarent', 400, "March-01-2020",'Server')
    restuarant.add_employee("server", server)

    # Show Employees:
    restuarant.add_employee("server",server)
    restuarant.show_employees()


    # print("Main As CPP")
#  Call the main:
Main()
print("\n")

# OR:

# if __name__ == "__main__":
#     Main()

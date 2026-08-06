from Menu import Pizza, Burger, Drinks, Menu
from Restuarant_sub import Restuarant
from Restuarant_Project import Chef, Customer, Server, Manager
from Order import Order

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
    restuarant.show_employees()

    # Customer 1 placing an order
    customer_1 = Customer("Sakib al Hasan", 456734356, "Sakib@m.com", "Banani", 1000000)
    order_1 =  Order(customer_1, [pizza_3, coffee])
    customer_1.pay_for_order(order_1)
    restuarant.add_order(order_1)

    # Customer 1 paying for order_1:
    restuarant.receive_payment(order_1, 2000, customer_1)

    print("Revenue & Balance After First Customer : ", restuarant.revenue, restuarant.balance)


    # Customer 2 placing an order
    customer_2 = Customer("Mashrafe Bin Mortaza", 454398586, "Sakib@m.com", "Banani", 1000000)
    order_2 =  Order(customer_2, [pizza_1, burger_2, coffee])
    customer_2.pay_for_order(order_2)
    restuarant.add_order(order_2)

  # Customer 1 paying for order_1:
    restuarant.receive_payment(order_2, 3000, customer_2)    
    print("Revenue & Balance After Second Customer : ", restuarant.revenue, restuarant.balance)




    # Pay rent:
    restuarant.pay_expense(restuarant.rent,"Rent")
    print("After Rent : ", restuarant.revenue, restuarant.balance, restuarant.expense)



    restuarant.pay_salary(chef)
    print("After salary : ", restuarant.revenue, restuarant.balance, restuarant.expense)





    # print("Main As CPP")
#  Call the main:
Main()
print("\n")

# OR:

# if __name__ == "__main__":
#     Main()

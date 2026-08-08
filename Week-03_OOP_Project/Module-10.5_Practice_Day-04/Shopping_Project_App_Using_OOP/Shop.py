
class Shop:
    def __init__(self, name, rent, products = []) -> None:
        self.name_of_shop = name
        self.rent = rent
        self.products_buy = []
        self.products = products
        self.Cashier = None
        self.Delivery = None
        self.Manager = None
        self.Visitor_Boy = None
        self.revenue = 0        # খরচ বা ব্যয় বাদ দেওয়ার আগে পণ্য বা সেবা বিক্রি করে যে মোট টাকা বা অর্থ পাওয়া যায়
        self.expanse = 0
        self.balance = 0
        self.profit = 0


    def add_employee(self, employee_type, employee):
        self.empolyee_tpye = employee_type
        self.employee = employee
        if employee_type == "Cashier":
            self.Cashier = employee
        elif employee_type == "Delivery":
            self.Delivery = employee
        elif employee_type == "Manager":
            self.Manager = employee
        elif employee_type == "Visitor_Boy":
            self.Visitor_Boy = employee

    def buy_products(self, products):
        self.products_buy.append(products)

    def payment(self, product, amount):
        if amount > product.bill:
            self.revenue += product.bill
            self.balance += product.bill
            self.due_amount = 0
            return amount - product.bill
        else:
            print(f"Your account has no money!!")

    def pay_salary(self, employee):
        print(f"Employee is {employee.name} and his salary amount is {employee.salary}")
        if employee.salary < self.balance:
            self.balance -= employee.salary
            self.expanse += employee.salary
            employee.receive_salary()
        else:
            print(f"Your Account has not too much money to pay salary !!")

    def pay_expense(self, amount, description):
        if amount < self.balance:
            self.expanse += amount
            self.balance -= amount
            print(f"Expense is {amount} and Description is {description}")
        else:
            print(f"Not Enough money for this expense !!")

        
            





        
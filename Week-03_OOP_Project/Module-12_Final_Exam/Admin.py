from User import Main_Account, Transfer_Money, Loan

def admin():
    my_account = Main_Account("Showmik Sharma","showmik@mail.com","Kalidaha",34356)
    my_account.__current_balance = 100000

    money_transfer = Transfer_Money("Devgon","devgon@mail.com","Feni",50000)
    money_transfer.__current_balance = 5000

    loan = Loan("Dingon","dingon@.com","Bye Bye",450054)
    print(loan.loan_cnt)

    print(my_account.name)
    print(my_account.__current_balance)
    print(money_transfer.__current_balance)

if __name__ == "__main__":
    admin()



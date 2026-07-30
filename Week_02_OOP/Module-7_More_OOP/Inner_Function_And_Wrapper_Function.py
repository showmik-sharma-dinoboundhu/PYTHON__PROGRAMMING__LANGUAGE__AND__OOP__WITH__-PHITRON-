# In python function is a first class object

def double_decker():
    print("Starting the double dacter")
    def inner_fun():
        print("Inside the inner")
        return 3000
    return inner_fun

# print(double_decker())
# print(double_decker()())

def doSomething(work):
    print("Work Started")
    # print(work)
    work()
    print("Work ended")

# doSomething(2)
# doSomething("ami busy")

def codding():
    print("Codding with python")

# doSomething(codding)

def sleeping():
    print("Sleeping and Dreaming with python")

doSomething(sleeping)

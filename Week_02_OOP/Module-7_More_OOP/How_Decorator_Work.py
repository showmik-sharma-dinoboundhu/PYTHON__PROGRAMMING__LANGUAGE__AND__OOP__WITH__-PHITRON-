import math
import time

def timer(func):
    def inner(*args, **kargs):
        print("Time started")
        start = time.time()
        # print(func)
        func(*args, **kargs)
        print("Time ended")
        end = time.time()
        print(f"Toatl time taken : {end - start}")

    return inner
# timer()()

@timer
def get_factorial(n):
    print("Factorial Started")
    result = math.factorial(n)
    print(f"Factorial of {n} in : {result}")

get_factorial(n = 6)

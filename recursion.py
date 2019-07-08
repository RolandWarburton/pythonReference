# if i want to calculate a factorial of a number (eg. 5*4*3*2*1)
def factorial(x):
    if x == 1:
        return 1
    else:
        # call its-self and do x*x-1 over and over until its = 1
        return x * (factorial(x-1))


print(factorial(5))

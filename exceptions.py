# see the different exception types
# https://www.programiz.com/python-programming/exceptions
try:
    int("rip")
except ValueError:
    print("error!!")
finally:
    print("this always executes")

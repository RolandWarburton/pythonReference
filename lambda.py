
# a lambda is like an anonymous variable. does not have a name and always returns something

# squares the number given (10)
a = 10
square = (lambda x: x**2)(a)
print(square)

# can be written inline to
print((lambda x: x**2)(a))

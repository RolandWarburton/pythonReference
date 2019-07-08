def double(x):
    return x*2


# list to manipulate
a = [1, 2, 3, 4, 5]

# applies the function to the whole list
result = list(map(double, a))
print(result)

# you can also do this with a lambda
result = list(map(lambda x: x*2, a))
print(result)

# this wont work. it adds extra values, not manipulate the existing ones
test = double(a)
print(test)

# take 10% off everything in a list
a = [10, 20, 30, 40]
print(list(map(lambda x: x - (x * 10) / 100, a)))

# generators are used to create lists


# yield adds the number in question into the list
def even(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


# list() converts a thing to a list
result = list(even(20))
print(result)




def add_ten(x):
    return x+10


def run_twice(func, arg):
    # (func is a parameter) attempts to run the outside first which calls and returns the inside. then runs the outside
    # so the inside is given 10 and is turned into 20. then 20 is passed to the outside and 10 is added again
    return func(func(arg))


print(run_twice(add_ten, 10))

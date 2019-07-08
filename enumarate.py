# define an array to loop over
a = ["apples", "oranges", "pears", "limes", "lemons"]

# counter variable
i = 0
# this loop just prints everything in the array and keeps count of it
for element in a:
    print("i = {} element = {}".format(i, element))
    i = i + 1

print("\nenumerate example:")
# doing the same thing but with enumerate (implementing a counter)
for i, element in enumerate(a):
    print(element)
    # print(a[i]) also works

# removes the need to declare i outside of the loop
# takes each item in the list and gives it a number (creating a tuple)
# eg. (0, "apples") (1, "oranges")
# you can also say: a[i] and print the same thing. But its easier to use 'element' because it makes more sense

print("\nenumerate but starting from 100:")
# doing the same thing but with enumerate (implementing a counter)
for i, element in enumerate(a, 100):
    print("i = {} element = {}".format(i, element))

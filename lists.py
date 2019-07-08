a = [1, 2, 3, 4, 5]

# slice a list
print(a[2:5])

# get all the numbers from <index position
print(a[:2])

# slice with an interval
print(a[0:6:2])

# list comprehension
# this list generates the first 5 multiples of 2
b = [x*2 for x in range(5)]
print(b)

# this list generates the first 10 powers AND filters.py only even numbers
b = [x**2 for x in range(10) if x % 2 == 0]
print(b)


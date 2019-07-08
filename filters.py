# 1, 2, 3, 4 etc
a = range(0, 100)
b = [1, 2, 3]

# print only even
result = list(filter(lambda x: x % 2 == 0, a))
print(result)

# pick a number from a list
result = list(filter(lambda x: x == 1, b))
print(result)

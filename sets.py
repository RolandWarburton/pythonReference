# sets are like lists
# sets cannot contain duplicate elements

# you can declare a set like this
a = {1, 2, 3, 4, 5}
# or like this
a = set(range(0, 6))

# check for a number in the set
print("check for a number in the set")
print(2 in a)

# add a number to the set
print("add a number to the set")
a.add(9)
print(a)

# remove a number to the set
print("remove a number to the set")
a.remove(1)
print(a)

# union (combines with no dupes)
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print("set union")
print(a | b)

# intersection (finds common elements)
print("set intersection")
print(a & b)

# removes any vales present in b from a
print("set difference")
print(a - b)

a = 1
content = "number: {}".format(a)
print(content)

# setting the variable by targeting it
number = 100
print("{a}".format(a=number))

# put some content between things in a list
a = ["hello", "world", "three", "test"]
print(" and ".join(a))

# replace a target string. will NOT replace the string if it cannot find it (no error)
print("hello there".replace("there", "kenobi"))

# starting with or ending with
print("boys will be boys".startswith("boy"))
print("boys will be boys".endswith("boy"))

# transform to uppercase / lowercase
print("come here".upper())
print("COME here".lower())
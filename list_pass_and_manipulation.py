# prints the list with different features
def print_list(t):
    # print the whole list
    print("\nprinting the whole list: ")
    for i in t:
        print(i)

    # print a specific index
    print("\nprint a specific index")
    print(t[1])

    # append to a list
    print("\nappending to the list")
    # append is returned back to main
    try:
        t.append("appended")
    except ValueError:
        return False
    else:
        print("success")

    # insert to a list
    print("\ninsert to the list")
    try:
        t.insert(1, "inserted")
    except ValueError:
        return False
    else:
        print("success")

    # get the location of something in a list
    print("\nprint index of item")
    print(t.index("appended"))

    return True


# define the different list types
a = ["apple", "banana", "orange"]
b = list(range(1, 10))

# define the different lists to be selected (switch)
# 'a' is referring to the above list
choices = {
    1: a,
    2: b
}
# ask for a key
key = int(input("which list: "))
# execute the function with the selected list
print_list(choices.get(key, "fail"))

# get the length of a list
print("get the length of a list")
print(len(a))
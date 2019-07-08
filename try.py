
def func():
    # repeat until true
    while True:
        try:
            x = int(input("enter a number: "))
            # will only return true if no error. on faIl goes to except
            return True
        except ValueError:
            print("failed")


if func():
    print("ayy")


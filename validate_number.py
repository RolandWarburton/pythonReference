mark = input('enter mark ')

try:
    int(mark)
except ValueError:
    try:
        float(mark)
    except ValueError:
        print("This is not a number")


#simple version

mark = input("enter a number")

#test to see if theres an error
try:
    int(mark)
except ValueError:
    print('failed')

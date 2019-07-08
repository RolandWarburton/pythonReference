from tkinter import *
import parser

# globally declare the expression variable 
i = 0


def press(num):
    # point out the global expression variable 
    global i

    if i == 0:
        display.delete(0, END)

    # get the position 'i' and put the number there in the string
    display.insert(i, num)
    i += 1


def clear_screen():
    display.delete(0, END)


def undo():
    oldstring = display.get()
    if oldstring > 0:
        newstring = oldstring[:-1]
        clear_screen()
        display.insert(0, newstring)
    else:
        clear_screen()
        print("error")


# Function to evaluate the final expression 
def calculate():
    entire_string = display.get()
    # print(entire_string)
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_screen()
        display.insert(0, result)
    except ZeroDivisionError:
        clear_screen()
        display.insert(0, "Error")


# create a GUI window
root = Tk()

# set the title of GUI window
root.title("Simple Calculator")

# set the configuration of GUI window
root.geometry("265x125")


display = Entry(root)
display.insert(0, "enter stuff")
display.grid(columnspan=4, sticky=(E, W))


# create a Buttons and place at a particular
# location inside the root window .
# when user press the button, the command or
# function affiliated to that button is executed .
button1 = Button(root, text=' 1 ', fg='black', bg='red',
                 command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)

button2 = Button(root, text=' 2 ', fg='black', bg='red',
                 command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)

button3 = Button(root, text=' 3 ', fg='black', bg='red',
                 command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)

button4 = Button(root, text=' 4 ', fg='black', bg='red',
                 command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)

button5 = Button(root, text=' 5 ', fg='black', bg='red',
                 command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)

button6 = Button(root, text=' 6 ', fg='black', bg='red',
                 command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)

button7 = Button(root, text=' 7 ', fg='black', bg='red',
                 command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)

button8 = Button(root, text=' 8 ', fg='black', bg='red',
                 command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)

button9 = Button(root, text=' 9 ', fg='black', bg='red',
                 command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)

button0 = Button(root, text=' 0 ', fg='black', bg='red',
                 command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0)

plus = Button(root, text=' + ', fg='black', bg='red',
              command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3)

minus = Button(root, text=' - ', fg='black', bg='red',
               command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)

multiply = Button(root, text=' * ', fg='black', bg='red',
                  command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)

divide = Button(root, text=' / ', fg='black', bg='red',
                command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)

equal = Button(root, text=' = ', fg='black', bg='red',
               command=calculate, height=1, width=7)
equal.grid(row=5, column=2)

clear = Button(root, text='Clear', fg='black', bg='red',
               command=clear_screen, height=1, width=7)
clear.grid(row=5, column='1')

# start the root
root.mainloop()

from tkinter import *


def left_click(a):
    print("lefty")


def right_click(a):
    print("righty")


def middle_click(a):
    print("middle")


root = Tk()

# configure the window
root.rowconfigure(9, {'minsize': 30})
root.columnconfigure(9, {'minsize': 30})

# create the top frame
left_frame = Frame(root, width=300, height=250)

# create stuff
button_1 = Button(left_frame, text="button", bg="black", fg="white")
space_1 = Label(left_frame, bg="grey", text="testsetestesetesttes")
space_2 = Label(left_frame, bg="grey")

# place stuff
left_frame.grid(row=0, column=0)
space_1.grid(row=0, column=0)
space_2.grid(row=1, column=0)


button_1.grid(columnspan=5, row=3, sticky=E)
button_1.bind("<Button-1>", left_click)
button_1.bind("<Button-2>", middle_click)
button_1.bind("<Button-3>", right_click)

root.mainloop()



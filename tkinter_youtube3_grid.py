from tkinter import *


root = Tk()

# create the top frame
topframe = Frame(root)

# create stuff
label_1 = Label(topframe, text="hello there")
label_2 = Label(topframe, text="general kenobi")

entry_1 = Entry(topframe, bg="grey")
entry_2 = Entry(topframe)

c = Checkbutton(topframe, text="Keep me logged in")

# place stuff
topframe.grid(row=0, column=0)

label_1.grid(row=0, column=0, sticky=E)
label_2.grid(row=1, column=0, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c.grid(columnspan=2, row=2)

root.mainloop()



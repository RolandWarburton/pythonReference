from tkinter import *


def nothing():
    print("sup")


root = Tk()

# CREATE FRAME/S
content = Frame(root, width=300, height=300)
top_frame = Frame(content, width=300, height=350)
main_frame = Frame(root, bg="blue")
bottom_frame = Frame(root, bg="blue")

# configure
root.columnconfigure(0, weight=1)

# ======CREATE A DROPDOWN======
# make the menu
menu = Menu(top_frame)

# tell TK that this thing is a menu
root.config(menu=menu)

# declare a submenu - Menu(where do i put this menu)
submenu = Menu(menu, tearoff=0)

# create the drop down
menu.add_cascade(label="click me", menu=submenu)

# put things in the submenu
submenu.add_command(label="one", command=nothing)
submenu.add_separator()
submenu.add_command(label="two", command=nothing)

# ======CREATE A TOOLBAR======
toolbar = Frame(main_frame, bg="blue")
insertbutt1 = Button(toolbar, text="butt 1", command=nothing)
insertbutt2 = Button(toolbar, text="butt 2", command=nothing)
insertbutt3 = Button(toolbar, text="butt 3", command=nothing)


# ======CREATE A STATUS BAR======

status = Label(bottom_frame, text="preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)


# place things
top_frame.grid(row=0, column=0)

# placing the tool bar
# the main frame sticks up the top left all the time (NW)
main_frame.grid(row=0, column=0, sticky=N+E+W)

toolbar.grid(row=0, column=0)
insertbutt1.pack(side=LEFT)
insertbutt2.pack(side=LEFT)
insertbutt3.pack(side=LEFT)

# placing the status bar
bottom_frame.grid(row=0, column=0, sticky=S+E+W)
status.grid(row=0, column=0, sticky=S)

root.mainloop()
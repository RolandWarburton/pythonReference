from tkinter import *

root = Tk()
root.title("Base")
# frames
top_frame = Frame(root, bg="orange")
bottom_frame = Frame(root, bg="purple")
middle_frame = Frame(root, bg="black")
left_frame = Frame(middle_frame, bg="grey")

# ================== CONFIG FRAMES ==================
# make the top go up the top (N), and stretch to each side (E, W)
top_frame.grid(row=0, sticky=(N, E, W))
# make the bottom go down the bottom (N), and stretch to each side (E, W)
bottom_frame.grid(row=2, sticky=(S, E, W))
# make the middle window expand to fill
middle_frame.grid(row=1, sticky=(N, S, E, W))
# make the LEFT window expand to fill
left_frame.pack(side=LEFT, fill=Y)


# make the 'root' fill the whole window (we put the 'content' frame inside and everything else stretches to fit inside)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# set the size of the window
root.minsize(500, 300)


# # ================== CONTENT ==================

# dimension labels
# top_lbl = Label(top_frame, text="top", bg="purple")
# bottom_lbl = Label(bottom_frame, text="bottom", bg="yellow")
middle_lbl = Label(middle_frame, text="middle", bg="blue")
left_lbl = Label(left_frame, text="left label", bg="magenta")

# top_lbl.pack()
# bottom_lbl.pack(padx=54)
middle_lbl.pack()
left_lbl.pack()

# STATUS BAR ==================
status = Label(bottom_frame, text="status bar yo", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# DROP DOWN ==================
# make the menu
menu = Menu(top_frame)

# tell TK that this thing is a menu
root.config(menu=menu)

# declare a submenu on 'menu'
submenu = Menu(menu, tearoff=0, fg="red")

# create the drop down
menu.add_cascade(label="click me", menu=submenu)

# put things in the submenu
submenu.add_command(label="one")
submenu.add_separator()
submenu.add_command(label="two")

# TOOLBAR ==================
toolbar = Frame(top_frame, bg="blue")
tool_button_1 = Button(toolbar, text="butt 1")
tool_button_2 = Button(toolbar, text="butt 2")
tool_button_3 = Button(toolbar, text="butt 3")

toolbar.pack(side=LEFT)
tool_button_1.pack(side=LEFT)
tool_button_2.pack(side=LEFT)
tool_button_3.pack(side=LEFT)


root.mainloop()

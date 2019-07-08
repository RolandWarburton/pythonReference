from tkinter import *


root = Tk()
# create the top and bottom frame
topframe = Frame(root)
bottomframe = Frame(root)

# create a label (BLACK) and button (RED)
one = Label(topframe, bg="black", fg="white")
entry = Entry(one)
button1 = Button(one, text="button1", bg="red")
button2 = Button(bottomframe, text="button2", bg="blue")


topframe.pack(fill=BOTH)
one.pack(fill=BOTH)
entry.pack(side=LEFT)
button1.pack(side=LEFT)

bottomframe.pack(side=BOTTOM)
button2.pack(side=BOTTOM)



root.mainloop()

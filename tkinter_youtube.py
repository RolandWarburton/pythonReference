from tkinter import *


root = Tk()
topframe = Frame(root)
bottomframe = Frame(root)

topframe.pack()
bottomframe.pack(side=BOTTOM)

button1 = Button(topframe, text="button1", bg="red")
button2 = Button(topframe, text="button2", bg="blue")
button3 = Button(topframe, text="button3", bg="green")
button4 = Button(bottomframe, text="button4", bg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()

from tkinter import *

root = Tk()

text1 = Label(root, text="pin")
text2 = Label(root, text="credit card number")

entry1 = Entry(root)
entry2 = Entry(root)

text1.grid(row=0, column=0)
text2.grid(row=1, column=0)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

root.mainloop()

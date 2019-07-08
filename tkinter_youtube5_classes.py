from tkinter import *


class Mybuttons:
    def __init__(self, master):
        top_frame = Frame(master)
        top_frame.grid(row=0, column=0)

        self.printbutton = Button(top_frame, text="click me", command=self.printmessage)
        self.printbutton.grid(row=0, column=0, sticky=W)

        self.quitbutton = Button(top_frame, text="quit", command=top_frame.quit)
        self.quitbutton.grid(row=0, column=1, sticky=E)

    def printmessage(self):
        print("ok cool")


root = Tk()
a = Mybuttons(root)
root.mainloop()

from tkinter import *


class MyButtons:

    def __init__(self, rootone):
        frame1 = Frame(rootone)
        frame1.place()

        self.printbutton = Button(frame1, text="Click Here", command=self.printmessage)
        self.printbutton.pack()

        self.quitbutton = Button(frame1, text="quit", command=frame1.quit)
        self.quitbutton.pack(side=LEFT)

    def printmessage(self):
        print("button clicked")


root = Tk()
root.title('Roland sucks at code')
b = MyButtons(root)

root.mainloop()

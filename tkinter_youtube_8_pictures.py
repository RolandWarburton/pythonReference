from tkinter import *

class Base:
    def __init__(self, master, top, bottom, middle, left):
        # ================== CONFIG FRAMES ==================
        # make the top go up the top (N), and stretch to each side (E, W)
        top.grid(row=0, sticky=(N, E, W))
        # make the bottom go down the bottom (N), and stretch to each side (E, W)
        bottom.grid(row=2, sticky=(S, E, W))
        # make the middle window expand to fill
        middle.grid(row=1, sticky=(N, S, E, W))
        # make the LEFT window expand to fill
        left.pack(side=LEFT, fill=Y)

        # make the 'root' fill the whole window
        # (we put the 'content' frame inside and everything else stretches to fit inside)
        master.columnconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)


root = Tk()
# frames
top_frame = Frame(root, bg="orange")
bottom_frame = Frame(root, bg="purple")
middle_frame = Frame(root, bg="black")
left_frame = Frame(middle_frame, bg="grey")

Base(root, top_frame, bottom_frame, middle_frame, left_frame)

# labels etc
top_lbl = Label(top_frame, text="top", bg="purple")
bottom_lbl = Label(bottom_frame, text="bottom", bg="yellow")
middle_lbl = Label(middle_frame, text="middle", bg="blue")
left_lbl = Label(left_frame, text="left label", bg="magenta")

# place the labels
top_lbl.pack()
bottom_lbl.pack()
middle_lbl.pack(side=TOP)
left_lbl.pack()

# pictures
photo = PhotoImage(file="SHNjFHw.png")
photo_lbl = Label(middle_frame, image=photo)
photo_lbl.pack(side=BOTTOM)

# canvas
canvas_one = Canvas(middle_frame, width=500, height=200)
canvas_one.pack(padx=20, pady=20, fill=BOTH, expand=TRUE, side=BOTTOM)

red_line = canvas_one.create_line(100, 100, 300, 300, width="5", fill="red")
black_line = canvas_one.create_line(100, 100, 300, 300, width="5", fill="black")
empty_rectangle = canvas_one.create_rectangle(25, 25, 310, 310)

canvas_one.delete(black_line)
# canvas_one.delete(ALL)




root.mainloop()

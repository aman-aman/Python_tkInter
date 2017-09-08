from tkinter import *

top=Tk()

def leftclick(event):
    print("left")
    
def rightclick(event):
    print("right")


frame = Frame(top,width=600,height=400)
frame.bind("<Button-1>",leftclick)
frame.bind("<Button-2>",rightclick)
frame.pack()

top.mainloop()

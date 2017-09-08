from tkinter import *

top = Tk()
def helloCallBack():
    tkMessageBox.showinfo( "Hello Python", "Hello World")
B = Tk.Button(top, text ="Hello", command = helloCallBack)
B.pack()
top.mainloop()

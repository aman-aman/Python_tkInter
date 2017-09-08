from tkinter import *
top=Tk()
def printName():
    print("hello iam aman")

#connecting a function to a button
buttoin1=Button(top,text="click..!!!",command=printName)
buttoin1.pack()

top.mainloop()

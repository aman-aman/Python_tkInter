from tkinter import *
top =Tk()
one=Label(top,text="one",bg="red")
one.pack(side=LEFT)
two=Label(top,text="two",bg="green")
#here X means fill in x directoion
two.pack(side=LEFT,fill=X)
two=Label(top,text="three",bg="purple")
#here y means fill in y directoion
two.pack(side=LEFT,fill=Y)
top.mainloop()

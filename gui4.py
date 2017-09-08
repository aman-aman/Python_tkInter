from tkinter import *
root=Tk()
#topFrame=Frame(root)
#topFrame.pack()
#bottomFrame=Frame(root)
#bottomFrame.pack(side=BOTTOM)

button1=Button(root,text="button 1",fg="red")
button2=Button(root,text="button 2",fg="blue")
button3=Button(root,text="button 3",fg="green")
button4=Button(root,text="button 4",fg="purple")

#button1.pack(side=LEFT)
#button2.pack(side=LEFT)
#button3.pack(side=LEFT)
#button4.pack(side=BOTTOM)

button1.pack()
button2.pack()
button3.pack()
button4.pack()

button1.tkMessagebox(top,text="aman1")
button2.tkMessagebox(top,text="aman2")
button3.tkMessagebox(top,text="aman3")
button4.tkMessagebox(top,text="aman4")

root.mainloop()

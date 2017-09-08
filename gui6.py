from tkinter import *


top =Tk()


label1_1=Label(top,text="Name")
label2_2=Label(top,text="Password")

#Entry is used to take tke input
entry_1=Entry(top)
entry_2=Entry(top)

#button
button1=Button(top,text="click me...!!!")

#grid is method to place
# E ,W,N,S EAST WEST NORTH SOUTH FOR ALINGMENT
label1_1.grid(row=0,sticky=E)
label2_2.grid(row=1,sticky=E)

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)


button1.grid(row=2,column=2)

c=Checkbutton(top,text="keep logged in")
#column span is used to merge column and span it to ither column
c.grid(columnspan=3)

top.mainloop()

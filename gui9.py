from tkinter import *


class aman:
    #master mean in top
    def __init__( self , master ):
        frame=Frame(master,width=600,height=300)
        frame.pack()

        
        self.printButton=Button(frame,text="message...!!!",command=self.printmessage)
        self.printButton.pack(side=LEFT)


        self.quitbutton=Button(frame,text="quit",command=frame.quit)
        self.quitbutton.pack(side=LEFT)
        
    def printmessage(self):
        n=input('enter your text to print')
        print(n)

        
top=Tk()
obj=aman(top)
top.mainloop()

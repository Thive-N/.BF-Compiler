from tkinter import Frame,Tk,Button,Text,END,Scale,VERTICAL,E
import time

class App:
  def __init__(self, master):
    self.frame = Frame(master)
    self.frame.grid()
    self.Bf_Text=""

    self.listframe=Frame(master)
    self.listframe.grid(column=0,row=1)

    self.CellText=Text(self.listframe,height=10,width=110)
    self.CellText.grid(column=0,row=0)

    self.w2 = Scale(self.frame, from_=0, to=1000,length=400, orient=VERTICAL)
    self.w2.grid(column=2)

    self.Bf_Code=Text(self.frame)
    self.Bf_Code.grid(column=0,row=0)
    
    self.Compile=Button(self.frame,width=20,text="Compile")
    self.Compile.grid(column=0,row=1)
    
    self.Output=Text(self.frame,width=30)
    self.Output.grid(column=1,row=0)

    self.ClearOutput=Button(self.frame,text="Clear Output")
    self.ClearOutput.grid(column = 1 , row = 1)




root = Tk()
app = App(root)
root.mainloop()

from tkinter import Frame,Tk,Button,Text,END,Scale,VERTICAL,E
import time

class App:
    def __init__(self, master):
        self.Bf_Text=""      
        self.frame = Frame(master) #frame for the main application including output input and time delay
        self.frame.grid()

        self.listframe=Frame(master) #seperate frame for the self.celltext at the bottom
        self.listframe.grid(column=0,row=1)

        #assigning the widgets to the frame
        #----------------------------------------------------------------------------------------------
        self.CellText=Text(self.listframe,height=10,width=115)
        self.CellText.grid(column=0,row=0)

        self.TimeDelay = Scale(self.frame, from_=0, to=1000,length=400, orient=VERTICAL)
        self.TimeDelay.grid(column=2)

        self.Bf_Code=Text(self.frame)
        self.Bf_Code.grid(column=0,row=0)

        self.Compile=Button(self.frame,width=20,text="Compile",command=self.RunEvaluation).grid(column=0,row=1)
        self.Output=Text(self.frame,width=30)
        self.Output.grid(column=1,row=0)
        self.ClearOutput=Button(self.frame,text="Clear Output", command=self.clear_output)
        self.ClearOutput.grid(column = 1 , row = 1)
        #----------------------------------------------------------------------------------------------




    def clear_output(self):
        if self.Read == False:
            self.Output.delete("0.0", "end")
        
    def Update_Lists(self):
        text=""
        for y in self.Cells:
            text=text+str(y)
            text+=" "


        self.CellText.delete(0.0,END)
        self.CellText.insert(0.0,text)
        self.highlight()


    def highlight(self):

        text=self.CellText.get(0.0,END)
        Vals=[]
        FindEnd = False
        LightMap = []

        
        for x,y in enumerate(text):
            if y == " ":
                Vals.append([y,x])
            else:
                Vals.append([y,x])
                

        if self.Pointer_C == 0:

            FindEnd = True
            LightMap.append(0)

        COUNt = 0
        for x in Vals:
            if x[0] == " ":
                COUNt += 1
            if FindEnd == False and x[0] == " " and COUNt == self.Pointer_C:
                LightMap.append(x[1]+1)     
                FindEnd = True     
                
            elif FindEnd == True and x[0] == " ":
                LightMap.append(x[1])

                break
        #light map is pointers for first and second " "

        left = "1."+str(LightMap[0])
        right = "1."+str(LightMap[1])

        self.CellText.tag_delete("highlight")
        self.CellText.tag_add("highlight", left , right)
        self.CellText.tag_configure("highlight" , background="yellow")

    def find_pairs(self,program): # put self before program to enable class compatibility + REQIREMENTS.txt
    

        """Returns a dict object containing the start and ends
        of each set of square brackets.
        """
        pairs = {}
        stack = []

        for i, c in enumerate(program):
            if c == '[':
                stack.append(i)
            elif c == ']':
                if len(stack) == 0:
                    self.Output.insert(END,"Error: No matching opening bracket for %i" % i +"\n -------END-------\n")
                pairs[stack.pop()] = i

        if len(stack) > 0:
            self.Output.insert(END,"Error: No matching opening bracket for %i" % i +"\n-------END-------\n")

        return pairs

  
    def CleanText(self,text):
        text = text.replace("\n","")
        text = text.replace(" ","")
        text = text.replace("\t","")
        text = text+"`" # to show where the end of the text is
        return text

    def RunEvaluation(self):
        self.Bf_Text=self.Bf_Code.get(0.0,END)
        self.Bf_Text=self.CleanText(self.Bf_Text)
        self.Pointer_C=0
        self.Pointer_D=0
        self.Cells=[0 for x in range(20000)]
        self.Read=True
        self.Delay=self.TimeDelay.get()
        self.LoopMap=self.find_pairs(self.Bf_Text)
        self.Execute()
        
    
    def Execute(self):
        self.Update_Lists()
        self.Current_Data = self.Bf_Text[self.Pointer_D]
        if self.Read == True:
            
            # logic goes here

            #moving the cell pointers
            if self.Current_Data == ">":
                self.Pointer_C += 1
            if self.Current_Data == "<":
                self.Pointer_C -=1
            

                  # Math

            if self.Current_Data == "+":
                self.Cells[self.Pointer_C] += 1
            if self.Current_Data == "-":
                self.Cells[self.Pointer_C] -= 1

                 #I/O

            if self.Current_Data == ".":
                self.Output.insert(END,"OUT: "+chr(int(self.Cells[self.Pointer_C])))
                self.Output.insert(END,"\n")
            if self.Current_Data == ",": 
                print("unimplemented")

            
                  #loop logic

            if self.Current_Data == "[":
                if self.Cells[self.Pointer_C] == 0 :
                    self.Pointer_D = self.LoopMap[self.Pointer_D]
    

            if self.Current_Data == "]":
                if self.Cells[self.Pointer_C] != 0 :
                    for key, val in self.LoopMap.items():
                        if val == self.Pointer_D:
                            self.Pointer_D = key





            if self.Current_Data == "`":
                print("ending")
                self.Output.insert(END,"-------END-------\n")
                self.Read = False
            else:
                self.Pointer_D += 1
                self.frame.after(self.Delay,self.Execute)
      
      
      

root = Tk()
app = App(root)
root.mainloop()

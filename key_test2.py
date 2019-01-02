from tkinter import *
class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.go = False
        self.btn = Button(text="Forwards", bg="grey", width=3)
        self.btn.bind('<Button-1>', self.showJudgments)
        self.btn.bind('<ButtonRelease-1>', self.makeChoice)
        self.btn.pack()
        self.pack(expand=YES, fill=BOTH)
        self.focus_force()
    def showJudgments(self, event=None):
        if self.go == False:
            self.go = True
            self.showJudgmentsA()
        else: 
            self.keepShowing()
            
    def keepShowing(self):
        print("a key being pressed")
    def showJudgmentsA(self):
        print("key-press started")
    def makeChoice(self, event=None):
        print("choice made")
        self.go = False
mainw = Tk()
mainw.f = MyFrame(mainw)
#mainw.f.grid()
mainw.mainloop()
from tkinter import *
import threading
from SpiderInit import SpiderInit
#from ServoControll import *
from SpiderBot import *
class MainWindow():
    def __init__(self):
        self.bla=0
        #threading.Thread.__init__(self)
        #self.start()
    def run(self):
        root = Tk()
        self.frame = Frame(root)
        self.frame.pack()
        self.InitButton = Button(self.frame, text="Init", bg="grey", width=3, command = lambda: SpiderInit())
        self.StartButton = Button(self.frame, text="Start", bg="grey", width=3, command = lambda: (SMoves = SpiderMoves()))
        self.ForwardButton = Button(self.frame, text="Forwards", bg="grey", width=3, command = lambda: forward_action(True))
        self.LeftButton = Button(self.frame, text="Left", bg="grey", width=3)
        self.RightButton = Button(self.frame, text="Right", bg="grey", width=3)
        self.BackButton = Button(self.frame, text="Backwards", bg="grey", width=3)
        self.ResetButton = Button(self.frame, text="Reset", bg="grey", width=3, command = lambda: reset_servos())
        self.StartButton.grid(row=1,column=3)
        self.ForwardButton.grid(row=3,column=3)
        self.LeftButton.grid(row=4,column=2)
        self.RightButton.grid(row=4,column=4)
        self.BackButton.grid(row=5,column=3)
        self.ResetButton.grid(row=2,column=3)
        if(self.forward):
            SMoves.move_forward()
        root.mainloop()
        
    def forward_action(self,pressed):
        self.forward = pressed
        
if __name__ == "__main__":
    mw = MainWindow()
    mw.run()
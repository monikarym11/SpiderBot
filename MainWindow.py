from tkinter import *
import threading
from SpiderInit import SpiderInit
from ServoControll import *
from SpiderBot import *

class MainWindow():
    def __init__(self):
        self.bla=0
        #threading.Thread.__init__(self)
        
        forward = False
        #self.start()
    def run(self):
        root = Tk()
        self.frame = Frame(root)

        
        #self.InitButton = Button(self.frame, text="Init", bg="grey", width=3, command = lambda: init_spider())
        self.InitButton = Button(self.frame, text="Init", bg="grey", width=3)
        #self.StartButton = Button(self.frame, text="Start", bg="grey", width=3, command = lambda: start_spider())

        self.StartButton = Button(self.frame, text="Start", bg="grey", width=3)
        self.ForwardButton = Button(self.frame, text="Forwards", bg="grey", width=3)
        self.LeftButton = Button(self.frame, text="Left", bg="grey", width=3)
        self.RightButton = Button(self.frame, text="Right", bg="grey", width=3)
        self.BackButton = Button(self.frame, text="Backwards", bg="grey", width=3)
        #self.ResetButton = Button(self.frame, text="Reset", bg="grey", width=3, command = lambda: reset_servos())
        self.ResetButton = Button(self.frame, text="Reset", bg="grey", width=3)
        self.StartButton.grid(row=1,column=3)
        self.ForwardButton.grid(row=3,column=3)
        self.LeftButton.grid(row=4,column=2)
        self.RightButton.grid(row=4,column=4)
        self.BackButton.grid(row=5,column=3)
        self.ResetButton.grid(row=2,column=3)

        self.ForwardButton.bind("<Button-1>", self.forward_action)
        self.frame.pack()

        #if(self.forward):
        #    SMoves.move_forward()
        root.mainloop()
        

    def forward_action(self, event):
        forward = True
        
        while(forward):
            # try:
            #    self.ForwardButton.bind("<ButtonRelease-1>", self.stop_action)
            #    print("pressed")
            # except KeyboardInterrupt:
            #     break
            print(forward)
            self.ForwardButton.bind("<ButtonRelease-1>", self.stop_action)
    def stop_action(self, event):
        forward = False
        print("released")

        
    def start_spider(self):
        self.spider = SpiderMoves()
if __name__ == "__main__":
    mw = MainWindow()
    mw.run()
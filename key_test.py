from tkinter import *

#class MyBtn(tk.Button):
#class MyBtn(Button):
    # set function to call when pressed

       
#class Mainframe(tk.Frame):
class Mainframe():
    #def __init__(self,master,*args,**kwargs):
    def __init__(self):
        #tk.Frame.__init__(self,master,*args,**kwargs)
        self.pressed = False
        
        #self.btn = MyBtn(Button(text="Forwards", bg="grey", width=3))
        # create the button and set callback functions
    def run(self):
        root = Tk()
        self.frame = Frame(root)
        self.frame.pack()
        self.btn = Button(self.frame, text="Forwards", bg="grey", width=3)
        #self.btn.set_up(self.on_up)
        #self.btn.set_down(self.on_down)
        self.set_up(self.btn, self.on_up)
        self.set_down(self.btn, self.on_down)
        
        #self.tbtn.pack()
        self.btn.pack()
        print(self.pressed)
        #if(self.pressed):
            #print("pressed")
        root.mainloop()
        
    # function called when pressed
    def on_down(self,x):
        print("Button down")
        
        #self.pressed = True
    # function called when released
    def on_up(self,x):
        print("Button up")
        #self.pressed = False
        
    def set_down(self, button,fn):
        button.bind('<Button-1>',fn)
        #button.invoke()
        self.set_down(button, self.on_down)
     
    # set function to be called when released
    def set_up(self, button,fn):
        button.bind('<ButtonRelease-1>',fn)
        
#class App(tk.Tk):
    #def __init__(self):
    #    tk.Tk.__init__(self)
               
   #     self.title('My Button')
  #      self.geometry('250x50')
 #       mf = Mainframe(self)
#        if mf.btn.pressed:
#            print("pressed")
#        mf.pack()

# create and run an App object
if __name__ == "__main__":
    #App().mainloop()
    mw = Mainframe()
    mw.run()
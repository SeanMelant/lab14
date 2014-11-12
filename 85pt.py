#########################################
#
#         85pt - Boundary detection
#
#########################################
# Add a button to move to the right and make them work as you'd expect (repeating lab12)
# This time - make sure that pressing left or right does nothing if you are going
# to hit a "boundary" - i.e. the edge of the screen.
from Tkinter import *
root = Tk()
drawpadwidth = 480
drawpadheight = 320
drawpad = Canvas(root, width=drawpadwidth, height=drawpadheight, background='blue')
oval = drawpad.create_oval(160,160,320,320, fill="orange")
class MyApp:
	def __init__(self, parent):
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
       	        self.button1 = Button(self.myContainer1)
       	        self.button1.configure(text="left", background= "purple")
       	        self.button1.grid(row=2,column=0)
       	        self.button1.bind("<Button-1>", self.leftClicked)
       	        self.button2 = Button(self.myContainer1)
       	        self.button2.configure(text="right", background= "yellow")
       	        self.button2.grid(row=2,column=3)
       	        self.button2.bind("<Button-1>", self.rightClicked)												
		self.button1.bind("<Button-1>", self.leftClicked)
		drawpad.pack()
        def leftClicked(self, event):    
	   global oval 
	   global drawpad 
	   global drawpadwidth 
	   global drawpadheight 
	   x1,y1,x2,y2 = drawpad.coords(oval)
	   if x1 > 0:
	       drawpad.move(oval,-10,0)
        def rightClicked(self,event):
            global oval
            global drawpad
            global drawpadwidth
            x1,y1,x2,y2 = drawpad.coords(oval)
            if x2 < drawpad.winfo_width():
                drawpad.move(oval,10,0)
myapp = MyApp(root)
root.mainloop()
from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Frame')

frame = LabelFrame(root,text='Test',padx=50,pady=50)
frame.grid(row=0,column=0)
frame.pack(padx=20,pady=20)
b = Button(frame,text='Dont click me')
b.pack()


root.mainloop()
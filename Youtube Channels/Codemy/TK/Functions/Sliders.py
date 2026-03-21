from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Sliders')
root.geometry('400x400')

vertical = Scale(root,from_=0, to=2000)
vertical.pack()

horizontal = Scale(root,from_=0, to=2000,orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root,text=horizontal.get()).pack()

def slide():
    my_label = Label(root,text=horizontal.get()).pack()

my_btn = Button(root,text='Click',command=slide).pack()
    

root.mainloop()


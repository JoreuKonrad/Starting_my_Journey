from tkinter import *

root = Tk()
root.title('Simple Calculator')
root.geometry("400x400")

def show():
    myLabel = Label(root,text=var.get()).pack()


var = StringVar()

c = Checkbutton(root,text='This a checkbox', variable=var,onvalue='On',offvalue='Off')
var.set('lollyganging')
c.pack()


myButton = Button(root,text='Show Selection',command = show)
myButton.pack()

root.mainloop()
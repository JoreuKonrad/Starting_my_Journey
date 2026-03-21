from tkinter import *

root = Tk()

e = Entry(root,width=30,
          fg='Blue',borderwidth=4)
e.pack()
e.insert(0,'Enter You Name:')

def myClick():
    myLabel = Label(root, text='Hello ' + e.get() + '!')
    myLabel.pack()

myButton = Button(root,text='See the Magic',
                  padx=200,pady=200,
                  command = myClick,
                  fg='white',
                  bg='blue').pack()


root.mainloop()
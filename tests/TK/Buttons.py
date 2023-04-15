from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text='I CLIKED!')
    myLabel.pack()

myButton = Button(root,text='Click Me',
                  padx=200,pady=200,
                  command = myClick,
                  fg='white',
                  bg='blue').pack()


root.mainloop()
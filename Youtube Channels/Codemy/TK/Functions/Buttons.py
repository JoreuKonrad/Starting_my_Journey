from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text='Você é catinga. Clique aqui')
    myLabel.pack()

myButton = Button(root,text='Você é catinga!',
                  padx=200,pady=200,
                  command = myClick,
                  fg='white',
                  bg='blue').pack()


root.mainloop()
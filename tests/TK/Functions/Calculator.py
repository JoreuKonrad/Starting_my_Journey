from tkinter import *

root = Tk()
root.title('Simple Calculator')

e = Entry(root,width=35,
          fg='Blue',borderwidth=4)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
e.pack()

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
    

button_1 = Button(root, text='1', padx=40, pady=20, command= lambda:button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command= lambda:button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command= lambda:button_click(3))

button_4 = Button(root, text='4', padx=40, pady=20, command= lambda:button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command= lambda:button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command= lambda:button_click(6))

button_7 = Button(root, text='7', padx=40, pady=20, command= lambda:button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command= lambda:button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command= lambda:button_click(9))

button_0 = Button(root, text='0', padx=40, pady=20, command= lambda:button_click(0))
button_clear = Button(root, text='1', padx=40, pady=20, command= lambda:button_click(9))
button_add = Button(root, text='1', padx=40, pady=20, command= lambda:button_click(9))
button_equal = Button(root, text='1', padx=40, pady=20, command= lambda:button_click(9))







root.mainloop()
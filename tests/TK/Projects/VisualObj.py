# Import the library tkinter
from tkinter import *
import pandas as pd
from tkinter import ttk, filedialog
import os
from PIL import Image

root = Tk()
root.title("Teste App")
root.geometry("750x600")


# Frame 1
frame1 = LabelFrame(root, text="Imagem 1", bg="green",fg="white", padx=100, pady=100)
frame1.grid(row=0, column=0)
label_inframe1 = Label(frame1,text='TESTE1')
label_inframe1.pack()

# Frame 2
frame2 = LabelFrame(root, text="Imagem 2", bg="yellow", padx=100, pady=100)
frame2.grid(row=0, column=1)
label_inframe2 = Label(frame2,text='TESTE2')
label_inframe2.pack()

# Frame 3
frame3 = LabelFrame(root, text="Imagem 3", bg="blue",fg='white', padx=100, pady=100)
frame3.grid(row=0, column=2)
label_inframe3 = Label(frame3,text='TESTE3')
label_inframe3.pack()


my_tree = ttk.Treeview(root)
my_tree['columns'] = ('Marca','Nome','Formato','Borda','Superficie')

# Formating
my_tree.column('#0',width=0, minwidth=0)
my_tree.column('Marca',anchor=W,width=30)
my_tree.column('Nome',anchor=W,width=150)
my_tree.column('Formato',anchor=W,width=20)
my_tree.column('Borda',anchor=W,width=80)
my_tree.column('Superficie',anchor=W,width=80)

# Create headings
my_tree.heading('#0',text='',anchor=W)
my_tree.heading('Marca',text='Marca',anchor=W)
my_tree.heading('Nome', text='Nome',anchor=CENTER)
my_tree.heading('Formato',text='Formato',anchor=W)
my_tree.heading('Borda', text='Borda',anchor=CENTER)
my_tree.heading('Superficie',text='Superficie',anchor=W)




button_img1


# Datas

data = pd.read_excel('Table.xlsx',index_col=0)

for record in range(len(data)):
    my_tree.insert(parent='',index='end',text='',iid=record,values=(data.loc[record,'Marca'],data.loc[record,'Nome'],data.loc[record,'Formato'],data.loc[record,'Borda'],data.loc[record,'Superficie']))

 


my_tree.grid(row=1,column=0,columnspan=3,padx=10,pady=10,ipadx=100)

root.mainloop()

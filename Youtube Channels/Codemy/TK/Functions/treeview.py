from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Resize')
root.geometry('500x400')

my_tree = ttk.Treeview(root)


# Defining the columns
my_tree['columns'] = ('Name','ID','Favorite Pizza')

# Formating
my_tree.column('#0',width=120, minwidth=25)
my_tree.column('Name',anchor=W,width=120)
my_tree.column('ID',anchor=CENTER,width=80)
my_tree.column('Favorite Pizza',anchor=W,width=120)

# Create headings
my_tree.heading('#0',text='Label',anchor=W)
my_tree.heading('Name',text='Name',anchor=W)
my_tree.heading('ID', text='ID',anchor=CENTER)
my_tree.heading('Favorite Pizza',text='Favorite Pizza',anchor=W)

# Add data
data = [
    ['John',0,'Peperroni'],
    ['Joreu',1,'Calabreza'],
    ['Catinga',2,'N lembro'],
    ['Maik',3,'Qualquer coisa'],
    ['Peido',4,'Qualquer coisa']
]
'''
count = 0
for record in data:
    my_tree.insert(parent='',index='end',text='',iid=count,values=(record[0],record[1],record[2]))
    count += 1
'''

my_tree.insert(parent='',index='end',iid=0,text='',values=('John','1','Peperroni'))
my_tree.insert(parent='',index='end',iid=1,text='',values=('Joreu','2','Calabreza'))
my_tree.insert(parent='',index='end',iid=2,text='',values=('Catinga','3','N lembro'))
my_tree.insert(parent='',index='end',iid=3,text='',values=('Caetano','4','Qualquer coisa'))
my_tree.insert(parent='1',index='end',iid=4,text='',values=('Maik','2.1','Qualquer coisa'))
my_tree.insert(parent='4',index='end',iid=5,text='',values=('Peido','2.2','Qualquer coisa'))
my_tree.insert(parent='5',index='end',iid=6,text='',values=('Peidooooo','2.3','Qualquer coisa'))

my_tree.insert(parent='',index='end',iid=8,text='',values=('Caetano','4','Qualquer coisa'))
my_tree.insert(parent='1',index='end',iid=9,text='',values=('Maik','2.1','Qualquer coisa'))
my_tree.insert(parent='4',index='end',iid=10,text='',values=('Peido','2.2','Qualquer coisa'))
my_tree.insert(parent='5',index='end',iid=11,text='',values=('Peidooooo','2.3','Qualquer coisa'))
my_tree.insert(parent='2',index='end',iid=12,text='',values=('Caetano','4','Qualquer coisa'))
my_tree.insert(parent='1',index='end',iid=13,text='',values=('Maik','2.1','Qualquer coisa'))
my_tree.insert(parent='4',index='end',iid=14,text='',values=('Peido','2.2','Qualquer coisa'))
my_tree.insert(parent='5',index='end',iid=15,text='',values=('Peidooooo','2.3','Qualquer coisa'))


my_tree.pack(pady=20)


root.mainloop()
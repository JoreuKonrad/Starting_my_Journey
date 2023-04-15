from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('New Window')

def click_command():
    top = Toplevel()
    my_img = ImageTk.PhotoImage(Image.open('Imagem.jpg'))
    my_label = Label(top)

myButton = Button(root,text='Click Me',
                  padx=200,pady=200,
                  command = click_command(),
                  fg='white',
                  bg='blue').pack()



root.mainloop()
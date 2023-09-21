from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Images')

my_img = ImageTk.PhotoImage(Image.open('G:/Meu Drive/Pastas Compartilhadas/Catalogo Concorrencia/Eliane/0- Eliane Imagens/0 - Versao antiga/Manila Marfim AC.jpg'))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root,text='Exit Program',command=root.quit)
button_quit.pack()

root.mainloop()


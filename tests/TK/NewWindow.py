from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('New Window')

top = Toplevel()
my_img = ImageTk.PhotoImage(Image.open('Image.jpg'))
my_label = Label(top,)


root.mainloop()
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Resize')
root.geometry('400x400')

# Open
my_pic = Image.open('image.jpg')

#Resize
resized = my_pic.resize((30,22),Image.ANTIALIAS)

# Recreating
new_pic = ImageTk.PhotoImage(resized)

# Get into app
my_label = Label(root,image=new_pic)
my_label.pack(pady=20)


root.mainloop()
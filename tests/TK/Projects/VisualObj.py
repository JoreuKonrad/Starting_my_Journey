# Import the library tkinter
from tkinter import *
import pandas as pd
from tkinter import ttk, filedialog
import os
from PIL import Image

root = Tk()
root.title("Teste App")
root.geometry("1000x600")

# Nome colunas: Cod.	Nome	Tipo	Tamanho

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

frame_table = LabelFrame(root,text='Tabela',padx=100,pady=100)
frame_table.grid(row=1, column=0)
label_inframe2 = Label(frame_table,text='TESTE FRAME')
label_inframe2.pack()


root.mainloop()

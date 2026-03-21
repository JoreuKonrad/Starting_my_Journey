from  tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Teste')

conn = sqlite3.connect('address_book.db')

c = conn.cursor()

c.execute('''CREATE TABLE tableTeste(
          firstName text,
          lastName text,
          age int
          )
           ''')

conn.commit()

conn.close()

root.mainloop()


import tkinter as tk
import pandas as pd

# Load data from Excel file
data = pd.read_excel('Table.xlsx',index_col=0)

# Create a Tkinter window
window = tk.Tk()

# Create a loop to iterate through the rows in the dataframe
for index, row in data.iterrows():
    # Create a button for each row
    button = tk.Button(window, text=row['Nome'])
    # Pack the button to display it in the window
    button.pack()

# Run the main loop to display the window
window.mainloop()

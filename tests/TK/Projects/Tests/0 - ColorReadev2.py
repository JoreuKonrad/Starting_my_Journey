import os
from tkinter import *
from PIL import Image

# Define the directory containing the images
image_dir = "C:/Users/joreu.konrad/Documents/VS Code Workplaces/Starting My Journey/Starting_my_Journey/Tests/TK/Projects/Images/"

# Define the Tkinter window
root = Tk()
root.title("Image Color Table")

# Create a frame to hold the canvas and scrollbar
frame = Frame(root)
frame.pack(side=TOP)

# Create a canvas to display the images and color representations
canvas = Canvas(frame)
canvas.pack(side=LEFT)

# Create a scrollbar for the canvas
scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas to use the scrollbar
canvas.config(yscrollcommand=scrollbar.set)

# Create a table to display the color representation for each image
table = Frame(canvas)
canvas.create_window((0, 0), window=table, anchor='nw')

# Loop through each image in the directory
for i, filename in enumerate(os.listdir(image_dir)):
    # Open the image
    image = Image.open(os.path.join(image_dir, filename))

    # Resize the image to 50x50 pixels
    image = image.resize((50, 50))

    # Get the RGB values for each pixel in the image
    pixels = list(image.getdata())

    # Create a canvas to display the color representation
    canvas1 = Canvas(table, width=50, height=50)
    canvas1.grid(row=i, column=0)

    # Display the color representation
    for j, pixel in enumerate(pixels):
        x = j % 50
        y = j // 50
        canvas1.create_rectangle(x, y, x+1, y+1, fill="#{:02x}{:02x}{:02x}".format(*pixel), outline="")

    # Display the filename in the second column
    Label(table, text=filename).grid(row=i, column=1)

# Update the canvas scroll region
canvas.update_idletasks()
canvas.config(scrollregion=canvas.bbox('all'))

# Start the Tkinter event loop
root.mainloop()

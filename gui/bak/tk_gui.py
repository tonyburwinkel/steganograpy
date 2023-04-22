import sys
from tkinter import *
from PIL import Image, ImageTk

# Create Tkinter root window
root = Tk()

# Open the image file
image = Image.open(sys.argv[1])

# Create a PhotoImage object of the image
photo = ImageTk.PhotoImage(image)

# Create left pane with 1/3 width
left_pane = Frame(root, width=root.winfo_width()//3, height=root.winfo_height())
left_pane.place(relx=0, rely=0, anchor=NW)

# Create a Label widget with the image
label = Label(root, image=photo)
label.place(relx=0.33, rely=0, anchor=NW)

# Create buttons
button1 = Button(left_pane, text="Button 1")
button1.pack()

button2 = Button(left_pane, text="Button 2")
button2.pack()

button3 = Button(left_pane, text="Button 3")
button3.pack()

# Run the Tkinter main loop
root.mainloop()

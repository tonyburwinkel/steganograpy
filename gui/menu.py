from tkinter import *
import os
from PIL import Image, ImageTk
  
# Create object
root = Tk()
  
# Change the label text
def show():
    label.config( text = selected.get() )

def load_image():
	current = Image.open(selected.get())
	new_photo = ImageTk.PhotoImage(Image.open(f"{selected.get()}"))
	print(selected.get())
	label.config(image = new_photo)
	label.image=new_photo

# Dropdown menu options
options = list(filter(lambda x: x[-3:]=="ppm", os.listdir()))
  
# datatype of menu text (tkinter.StringVar())
selected = StringVar()
# initial menu text
selected.set(f"{options[0]}" )
  
# Create Dropdown menu
drop = OptionMenu( root , selected , *options )
drop.pack()
	
#label = Label(root, image=photo)
#label.pack()
  
# Create button (its window, its text, its event listener)
button = Button( root , text = "load" , command = load_image )
button.pack() 

# load an image to start with
label_init = ImageTk.PhotoImage(Image.open(f"{options[0]}"))
# Create Label
label = Label( root , image = label_init )
label.pack()

stego_text = Text(root, height = 5, width = 52)
stego_text.pack()

save_name = Text(root, height = 1, width = 40)
save_name.pack()

'''
event handler for encode button
gets the text from stego_text and save_name
do what you want with them
clear the boxes
'''
def encode_image():
	print("encoding image!")
	text = stego_text.get("1.0", "end-1c")
	with open(f"{save_name.get('1.0', 'end-1c')}", "w") as f:
		f.write(text)
	
	stego_text.delete("1.0","end")

	print(text)

encode = Button( root , text = "encode", command = encode_image )
encode.pack() 
  
# Execute tkinter
root.mainloop()

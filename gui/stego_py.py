from tkinter import *
import tkinter as tk
import os
from PIL import Image
from PIL import ImageTk
  
# Create object
  
def decode_image():
	from image_decoder import ImageDecoder
	encoder = ImageDecoder(selected.get())
	message = encoder.msg
	stego_text.delete("1.0", "end")
	stego_text.insert("1.0", message)

def encode_image():
	text = stego_text.get("1.0", "end-1c")
	name = save_name.get("1.0", "end-1c")
	print(name)
	from image_encoder import ImageEncoder
	encoder = ImageEncoder(text,  f"{selected.get()}")
	encoder.create_steg_img()
	encoder.save_steg_image(f"{name}.ppm")
	clear_text()
	refresh_drop()

def refresh_drop():
	# Reset var and delete all old options
	selected.set('')
	drop['menu'].delete(0, 'end')

	# Insert list of new options (tk._setit hooks them up to var)
	new_choices = list(filter(lambda x: x[-3:]=="ppm", os.listdir()))
	for choice in new_choices:
		drop['menu'].add_command(label=choice, command=tk._setit(selected, choice))
	selected.set("choose image")

def load_image():
	current = Image.open(selected.get())
	new_photo = ImageTk.PhotoImage(Image.open(f"{selected.get()}"))
	print(selected.get())
	picture.config(image = new_photo)
	picture.image=new_photo
	clear_text()

def clear_text():
	print("clear")
	stego_text.delete("1.0","end")
	save_name.delete("1.0","end")

def exit_app():
	root.destroy()
	exit(1)

root = Tk()

# make a list of  options to fill the drop menu with
options = list(filter(lambda x: x[-3:]=="ppm", os.listdir()))
  
# datatype of menu text (tkinter.StringVar())
selected = StringVar()
# initial menu text
selected.set(f"{options[0]}" )
  
# Create Dropdown menu
drop = OptionMenu( root , selected , *options )
	
# Create load button (its parent, its text, its event listener)
load_btn = Button( root , text = "load" , command = load_image )
encode_btn = Button( root , text = "encode", command = encode_image )
decode_btn = Button( root , text = "decode", command = decode_image )
exit_button = Button(root, text="Exit", command=exit_app)

# load an image to start with
photo_init = ImageTk.PhotoImage(Image.open(f"{options[0]}"))
# Create Label with initial image to load
picture = Label( root , image = photo_init )

stego_text = Text(root, height = 5)

save_label = Label(root, text="encode as:")
save_name = Text(root, height = 1)

'''
drop.pack()
load_btn.pack(pady=10) 
picture.pack()
stego_text.pack(pady=10)
save_name.pack()
encode_btn.pack(pady=10) 
decode_btn.pack()
exit_button.pack(pady=20)
'''

drop.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
load_btn.grid(row=0, column=2, sticky="ew") 
picture.grid(row=1, column=0, columnspan=3, pady=10)
stego_text.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10)
save_label.grid(row=3, column=0)
save_name.grid(row=3, column=1, columnspan=2)
encode_btn.grid(row=4, column=0, sticky="ew") 
decode_btn.grid(row=4, column=1, sticky="ew")
exit_button.grid(row=4, column=2, sticky="ew")

# Execute tkinter
root.mainloop()

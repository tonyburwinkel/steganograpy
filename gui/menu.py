from tkinter import *
import tkinter as tk
import os
from PIL import Image
from PIL import ImageTk
  
# Create object
  
def mk_txt():
	print("encoding image!")
	text = stego_text.get("1.0", "end-1c")
	with open(f"{save_name.get('1.0', 'end-1c')}", "w") as f:
		f.write(text)
	
	stego_text.delete("1.0","end")

	print(text)

def decode_image():
	from image_decoder import ImageDecoder
	encoder = ImageDecoder(selected.get())
	message = encoder.msg
	stego_text.insert("1.0", message)
	print(message)

def encode_image():
	text = stego_text.get("1.0", "end-1c")
	stego_text.delete("1.0","end")
	name = save_name.get("1.0", "end-1c")
	save_name.delete("1.0","end")
	from image_encoder import ImageEncoder
	encoder = ImageEncoder(text,  f"{selected.get()}")
	encoder.create_steg_img()
	encoder.save_steg_image(f"{name}.ppm")
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
label_init = ImageTk.PhotoImage(Image.open(f"{options[0]}"))
# Create Label with initial image to load
picture = Label( root , image = label_init )

stego_text = Text(root, height = 5, width = 52)
save_name = Text(root, height = 1, width = 40)

drop.pack()
load_btn.pack(pady=10) 
picture.pack()
stego_text.pack(pady=10)
save_name.pack()
encode_btn.pack(pady=10) 
decode_btn.pack()
exit_button.pack(pady=20)
  
# Execute tkinter
root.mainloop()

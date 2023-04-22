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
	current = selected.get()
	selected.set('')
	drop['menu'].delete(0, 'end')

	# Insert list of new options (tk._setit hooks them up to var)
	new_choices = list(filter(lambda x: x[-3:]=="ppm", os.listdir()))
	for choice in new_choices:
		drop['menu'].add_command(label=choice, command=tk._setit(selected, choice))
	selected.set(current)

def load_image():
	current = Image.open(selected.get())
	new_photo = ImageTk.PhotoImage(Image.open(f"{selected.get()}"))
	print(selected.get())
	picture1.config(image = new_photo)
	picture1.image=new_photo
	picture2.config(image=None)
	picture2.image=None
	refresh_drop()

def make_lsb():
	current = selected.get()
	from lsb_expose import lsb_expose
	lsb_expose(current)
	lsb = ImageTk.PhotoImage(Image.open(f"{current.split('.')[0]}_lsb.ppm"))
	picture2.config(image = lsb)
	picture2.image = lsb

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
create_lsb = Button( root , text = "show lsb plane", command = make_lsb )
exit_button = Button(root, text="Exit", command=exit_app)

# load an image to start with
photo_init = ImageTk.PhotoImage(Image.open(f"{options[0]}"))
# Create Label with initial image to load
picture1 = Label( root , image = photo_init )
picture2 = Label( root , image = None )


'''
drop.pack()
load_btn.pack(pady=10) 
picture1.pack()
stego_text.pack(pady=10)
save_name.pack()
encode_btn.pack(pady=10) 
decode_btn.pack()
exit_button.pack(pady=20)
'''

#root.rowconfigure(0, weight=1)
#root.columnconfigure(0, weight=1)

drop.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
load_btn.grid(row=0, column=1, sticky="ew", padx=40) 
picture1.grid(row=1, column=0, pady=10, padx=30)
picture2.grid(row=1, column=1, pady=10, padx=30)
create_lsb.grid(row=4, column=0, sticky="ew") 
exit_button.grid(row=4, column=1, sticky="ew")

# Execute tkinter
root.mainloop()

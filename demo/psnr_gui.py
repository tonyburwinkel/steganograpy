from tkinter import *
import tkinter as tk
import os
from PIL import Image
from PIL import ImageTk
from psnr import get_psnr
  
def refresh_drop():
	# Reset var and delete all old options
	drop1['menu'].delete(0, 'end')
	drop2['menu'].delete(0, 'end')

	# Insert list of new options (tk._setit hooks them up to var)
	new_choices = os.listdir("ppm")
	for choice in new_choices:
		drop1['menu'].add_command(label=choice, command=tk._setit(selected1, choice))
		drop2['menu'].add_command(label=choice, command=tk._setit(selected2, choice))

def load_image():
	sel1 = f"ppm/{selected1.get()}"
	sel2 = f"ppm/{selected2.get()}"
	#current = Image.open(selected.get())
	pic1 = ImageTk.PhotoImage(Image.open(sel1))
	pic2 = ImageTk.PhotoImage(Image.open(sel2))
	picture1.config(image = pic1)
	picture1.image=pic1
	picture2.config(image=pic2)
	picture2.image=pic2
	psnr.config(text = f"PSNR = {get_psnr(sel1, sel2)}")
	refresh_drop()

def clear_text():
	print("clear")
	stego_text.delete("1.0","end")
	save_name.delete("1.0","end")

def exit_app():
	root.destroy()
	exit(1)

root = Tk()

# make a list of  options to fill the drop menu with
options = os.listdir("ppm")
  
# datatype of menu text (tkinter.StringVar())
selected1 = StringVar()
selected2 = StringVar()
# initial menu text
selected1.set(f"{options[0]}" )
selected2.set(f"{options[0]}" )
  
# Create Dropdown menu
drop1 = OptionMenu( root , selected1 , *options )
drop2 = OptionMenu( root , selected2 , *options )
	
# Create load button (its parent, its text, its event listener)
load_btn = Button( root , text = "load" , command = load_image )
# can pass params to command by using "lambda : my_func(args)"
#calculate = Button( root , text = "calculate", command = calc_psnr )
exit_button = Button(root, text="Exit", command=exit_app)

# load an image to start with
photo_init = ImageTk.PhotoImage(Image.open(f"ppm/{options[0]}"))
# Create Label with initial image to load
picture1 = Label( root , image = photo_init )
picture2 = Label( root , image = photo_init )
psnr_init = f"ppm/{options[0]}"
psnr = Label( root, text = f"PSNR = {get_psnr(psnr_init, psnr_init)}")


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

drop1.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
drop2.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
load_btn.grid(row=1, column=0, sticky="ew", padx=40) 
picture1.grid(row=2, column=0, pady=10, padx=30)
picture2.grid(row=2, column=1, pady=10, padx=30)
psnr.grid(row=3, column=0, pady=10, padx=10)
exit_button.grid(row=4, column=0, sticky="ew")

# Execute tkinter
root.mainloop()

import os
import tkinter as tk

def do_something_with_file(filename):
    print(f"Selected file: {filename}")

root = tk.Tk()

# Get a list of files in the working directory
files = os.listdir()
print(files)

# Create the dropdown menu and add each file as an option
menu = tk.Menu(root)
for filename in files:
    menu.add_command(label=filename, command=lambda f=filename: do_something_with_file(f))

# Create a button to open the dropdown menu
button = tk.Menubutton(root, text="Select a file", menu=menu)
button.pack()

root.mainloop()


from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import filemapper
import os
root = Tk()
screen_width, screen_height = (root.winfo_screenwidth(), root.winfo_screenheight())


def print_entry():
    
    path = path_entry.get()
    filemapper.scan_directory_recursive(path)
    parent_directory = "<" + os.path.basename(path) +"> \n"
    output_text.insert(1.0, str(parent_directory + filemapper.file_tree))

root.title =("File Mapper")
root.geometry(f"500x500+{int(screen_width/2 - 500/2)}+{int(screen_height/2 - 500/2)}") #makes sure the window is centered on screen


path_label = ttk.Label(root, text="Please enter directory path:")
path_label.pack(pady=2)

path = StringVar()
path_entry = ttk.Entry(root, width=40, textvariable=path) 
path_entry.pack(pady=5)

execute_button = ttk.Button(text="preess meee...", command=print_entry)
execute_button.pack(pady=5)

output_text = ScrolledText(root, width = 150, height=200)

output_text.pack(pady=10, expand=True)
# output_text = ttk.Label(root, text="Results will be displayed here:")
# output_text.pack(pady=10)

root.mainloop()
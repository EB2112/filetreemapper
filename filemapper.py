import os
from colorama import init
#from termcolor import colored



init()

file_tree = ""

path = "C:/Users/ezenb/Projects/python/filetree/testfolder"
#path=r"C:\Users\ezenb\Projects\python\filetree"
#parent_directory = "<" + os.path.basename(path) +">"

def scan_directory_recursive(path, depth=0):
    global file_tree
    for x in os.scandir(path):
        
        if x.is_dir():
            file_tree +=  " " * depth +  f"<{x.name}>\n"
            scan_directory_recursive(x.path, depth + 4)
        else:
                file_tree += " " * depth +  f"--{x.name}\n"
                #print(x.path)
    


def text_color(depth):
    if depth == 0:
         return 'green'
    elif depth == 2:
         return 'blue'
    elif depth % 2 == 0:
         return 'red'
    elif depth % 3 == 0:
         return 'yellow'
    else:
        return 'red'


scan_directory_recursive(path)
#print (parent_directory+"\n"+ file_tree)

def scan_directory(path):
    global file_tree
    file_tree += f" \n | {parent_directory}"
    for x in os.scandir(path):
        if x.is_dir():
              file_tree += f" \n | {x}"
              for y in os.scandir(x):
                   file_tree += f"--{y}"
        else:
            file_tree += f" \n | {x}"
    print(file_tree)


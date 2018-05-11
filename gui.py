import tkinter as tk
from tkinter import Menu
from tkinter import ttk


# Functions
# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()


# Procedural Code
# Create instance
win = tk.Tk()

# Add a title
win.title("Weather App")

# Creating a menubar
menuBar = Menu()
win.config(menu=menuBar)

# Add file menu
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

# Add Help menu
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
helpMenu.add_cascade(label="Help", menu=helpMenu)

# Add Tab Control









# Start GUI

win.mainloop()

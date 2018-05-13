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
tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Tab 1")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab 2")

tabControl.pack(expand=1, fill="both")

weather_conditions_frame = ttk.LabelFrame(tab1, text="Current Weather Conditions")
weather_conditions_frame.grid(column=0, row=0, padx=8, pady=4)

ttk.Label(weather_conditions_frame, text="Locations").grid(column=0, row=0, sticky="W")

city = tk.StringVar()
citySelected = ttk.Combobox(weather_conditions_frame, width=12, textvariable=city)
citySelected["values"]=("Los Angeles", "London", "Rio de Janeiro, Brazil")
citySelected.grid(column=1, row=0)
citySelected.current(0)



































































# Start GUI

win.mainloop()

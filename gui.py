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


max_width = max((len(x) for x in citySelected['values']))

ENTRY_WIDTH = max_width + 3

new_width = max_width - 4
citySelected.config(width=new_width)

ttk.Label(weather_conditions_frame, text="Last Updated:").grid(column=0, row=1, sticky='E')
updated = tk.StringVar()
updatedEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=updated, state='readonly')
updatedEntry.grid(column=1, row=1, sticky='W')

ttk.Label(weather_conditions_frame, text="Weather:").grid(column=0, row=2, sticky='E')
weather = tk.StringVar()
weatherEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=weather, state='readonly')
weatherEntry.grid(column=1, row=2, sticky='W')

ttk.Label(weather_conditions_frame, text="Temperature").grid(column=0, row=3, sticky='E')
temperature = tk.StringVar()
temperatureEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=temperature, state='readonly')
temperatureEntry.grid(column=1, row=3, sticky='W')

for child in weather_conditions_frame.winfo_children():
    # child.grid_configure(padx=6, pady=6)
    # child.grid_configure(padx=6, pady=3)
    child.grid_configure(padx=4, pady=2)


































































# Start GUI

win.mainloop()

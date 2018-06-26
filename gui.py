import tkinter as tk
from tkinter import Menu
from tkinter import ttk
from tkinter import scrolledtext
from weather-app.API_key import OWM_API_KEY
import urllib.request
import urllib.request import urlopen
import json
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pprint import pprint

#####################################################################
# Functions from all gui notebook tabs
#####################################################################

def get_open_weather_data(city='London,uk'):
    city = city.replace(' ', '%20')
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, OWM_API_KEY)
    response = urlopen(url)
    data = response.read().decode()
    json_data = json.loads(data)
    pprint(json_data)

    lat_long = json_data['coord']
    lastupdate_unix = json_data['dt']
    city_id = json_data['id']
    temp_kelvin = json_data['main']
    city_name = json_data['name']
    city_country = json_data['sys']['country']
    owm_weather = json_data['weather'][0]['description']
    weather


def get_weather_data(station_id='KLAX'):
    url_general = 'http://www.weather.gov/xml/current_obs/{}.xml'
    url = url_general.format(station_id)
    print(url)
    request = urllib.request.urlopen(url)
    content = request.read().decode()
    print(content)

    xml_root = ET.fromstring(content)
    print('xml_root: {}\n'.format(xml_root.tag))


    for datapoint in weather_data_tags_dict.keys():
        weather_data_tags_dict[datapoint] = xml_root.find(datapoint).text
    # use ElementTree to get certain tags from the xml

def populate_gui_from_dict():
    location.set(weather_data_tags_dict['location'])
    updated.set(weather_data_tags_dict['observation_time'].replace('Last Updated on ', ''))
    weather.set(weather_data_tags_dict['weather'])
    temp.set('{} \xb0F  ({} \xb0C)'.format(weather_data_tags_dict['temp_f'], weather_data_tags_dict['temp_c']))


def _get_station():
    station = station_id_combo.get()
    get_weather_data(station)
    populate_gui_from_dict()

def _get_cities():
    state = state_combo.get()
    get_city_station_ids(state)

def get_city_station_ids(state='ca'):
    url_general = 'http://w1.weather.gov/xml/current_obs/seek.php?state={}&Find=Find'
    state = state.lower()
    url = url_general.format(state)
    request = urllib.request.urlopen(url)
    content = request.read().decode()

    print(content)

    parser = WeatherHTMLParser()
    parser.feed(content)

    print(len(parser.stations) == len(parser.cities))

    scr.delete('1.0', tk.END) # Clear scrolledText widget for next button click

    # match the first item in them cities list to the first item in the stations list...and so on
    for idx in range(len(parser.stations)):
        city_station = parser.cities[idx] + ' (' + parser.stations[idx] + ')'  # insert parenthesis in between cities and stationid
        print(city_station)
        scr.insert(tk.INSERT, city_station + '\n')



# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()

###########################################################################################
# Classes from all gui notebook tabs
###########################################################################################

class WeatherHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stations = []
        self.cities = []
        self.grab_data = False

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if "display.php?stid=" in str(attr):
                cleaned_attr= str(attr).replace("('href', 'display.php?stid=", '').replace("')", '')
                self.stations.append(cleaned_attr)
                self.grab_data = True

    def handle_data(self, data):
        if self.grab_data:
            self.cities.append(data)
            self.grab_data = False





################################################################################################
# Procedural Code by organized by notebook tabs
###############################################################################################
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

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="NOAA")

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="Station ID Finder")

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Open Weather Map")


tabControl.pack(expand=1, fill="both")

# TAB 2 #############################################################################

weather_conditions_frame = ttk.LabelFrame(tab2, text="Current Weather Conditions")
weather_conditions_frame.grid(column=0, row=1, padx=8, pady=4)



ENTRY_WIDTH = 25

ttk.Label(weather_conditions_frame, text="Last Updated:").grid(column=0, row=1, sticky='E')
updated = tk.StringVar()
updatedEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=updated, state='readonly')
updatedEntry.grid(column=1, row=1, sticky='W')

ttk.Label(weather_conditions_frame, text="Weather:").grid(column=0, row=2, sticky='E')
weather = tk.StringVar()
weatherEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=weather, state='readonly')
weatherEntry.grid(column=1, row=2, sticky='W')

ttk.Label(weather_conditions_frame, text="Temperature").grid(column=0, row=3, sticky='E')
temp = tk.StringVar()
tempEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=temp, state='readonly')
tempEntry.grid(column=1, row=3, sticky='W')

for child in weather_conditions_frame.winfo_children():
    # child.grid_configure(padx=6, pady=6)
    # child.grid_configure(padx=6, pady=3)
    child.grid_configure(padx=4, pady=2)

weather_cities_frame = ttk.LabelFrame(tab1,text=' Latest Observation for ')
weather_cities_frame.grid(column=0, row=0,padx=8, pady=4)


ttk.Label(weather_cities_frame, text="Weather Station ID: ").grid(column=0, row=0)

station_id = tk.StringVar()
station_id_combo = ttk.Combobox(weather_cities_frame, width=6, textvariable=station_id)

station_id_combo['values'] = ('KLAX', 'KDEN', 'KNYC')
station_id_combo.grid(column=1, row=0)
station_id_combo.current(0)




location = tk.StringVar()
ttk.Label(weather_cities_frame, textvariable=location).grid(column=0, row=1, columnspan=3)

for child in weather_cities_frame.winfo_children():
    child.grid_configure(padx=5, pady=4)


get_weather_btn = ttk.Button(weather_cities_frame, text='Get Weather', command=_get_station).grid(column=2, row=0)


# NOAA DATA directly from live web search

#Retrieve the tags we are interested in
weather_data_tags_dict = {
    'observation_time': '',
    'weather': '',
    'temp_f': '',
    'temp_c': '',
    'location': '',
}

# TAB 3 ##########################################################################


# Create a container to hold all other widgets
weather_states_frame = ttk.Label(tab3, text= 'Weather Station IDs')
weather_states_frame.grid(column=0, row=0, padx=8, pady=4)

ttk.Label(weather_states_frame, text="Select a State: ").grid(column=0, row=0)

state =tk.StringVar()
state_combo = ttk.Combobox(weather_states_frame, width=5, textvariable=state)
state_combo['values'] = ('AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI',
                         'ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI',
                         'MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC',
                         'ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT',
                         'VT','VA','WA','WV','WI','WY'
                         )

state_combo.grid(column=1, row=0)
state_combo.current(0)

get_weather_btn = ttk.Button(weather_states_frame, text='Get Cities', command=_get_cities).grid(column=2, row=0)

scr = scrolledtext.ScrolledText(weather_states_frame, width=50, height=17, wrap=tk.WORD)
scr.grid(column=0, row=1, columnspan=3)


for child in weather_states_frame.winfo_children():
    child.grid_configure(padx=6, pady=6)


# TAB 1 ##########################################################################


weather_conditions_frame = ttk.LabelFrame(tab1, text="Current Weather Conditions")
weather_conditions_frame.grid(column=0, row=1, padx=8, pady=4)



ENTRY_WIDTH = 25

ttk.Label(weather_conditions_frame, text="Last Updated:").grid(column=0, row=1, sticky='E')
updated = tk.StringVar()
updatedEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=updated, state='readonly')
updatedEntry.grid(column=1, row=1, sticky='W')

ttk.Label(weather_conditions_frame, text="Weather:").grid(column=0, row=2, sticky='E')
weather = tk.StringVar()
weatherEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=weather, state='readonly')
weatherEntry.grid(column=1, row=2, sticky='W')

ttk.Label(weather_conditions_frame, text="Temperature").grid(column=0, row=3, sticky='E')
temp = tk.StringVar()
tempEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=temp, state='readonly')
tempEntry.grid(column=1, row=3, sticky='W')

for child in weather_conditions_frame.winfo_children():
    # child.grid_configure(padx=6, pady=6)
    # child.grid_configure(padx=6, pady=3)
    child.grid_configure(padx=4, pady=2)

weather_cities_frame = ttk.LabelFrame(tab1,text=' Latest Observation for ')
weather_cities_frame.grid(column=0, row=0,padx=8, pady=4)


ttk.Label(weather_cities_frame, text="Weather Station ID: ").grid(column=0, row=0)

station_id = tk.StringVar()
station_id_combo = ttk.Combobox(weather_cities_frame, width=6, textvariable=station_id)

station_id_combo['values'] = ('KLAX', 'KDEN', 'KNYC')
station_id_combo.grid(column=1, row=0)
station_id_combo.current(0)




location = tk.StringVar()
ttk.Label(weather_cities_frame, textvariable=location).grid(column=0, row=1, columnspan=3)

for child in weather_cities_frame.winfo_children():
    child.grid_configure(padx=5, pady=4)


get_weather_btn = ttk.Button(weather_cities_frame, text='Get Weather', command=_get_station).grid(column=2, row=0)


# NOAA DATA directly from live web search

#Retrieve the tags we are interested in
weather_data_tags_dict = {
    'observation_time': '',
    'weather': '',
    'temp_f': '',
    'temp_c': '',
    'location': '',
}









































































# Start GUI

win.mainloop()

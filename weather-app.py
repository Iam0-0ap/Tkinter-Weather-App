from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
import json


# import librareis related to time zone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

import requests
import os



screen = Tk()
screen.geometry("900x500+300+200")
screen.resizable(False, False)
screen.title('Weather App')


def getWeather():
    city = text_field.get()
    geolocator = Nominatim(user_agent='geoapiExercises')
    location = geolocator.geocode(city)
    obj= TimezoneFinder()
    result = obj.timezone_at(lng = location.longitude, lat = location.latitude)
    
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text = current_time)
    time.config(text = "CURRENT WEATHER")

    #api
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b2f1f7c244030cbc4e09464e3ce5ce60"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp']-273.15)
  
    
    print(json_data)
    t.config(text =(temp, "°"))
    c.config(text= (condition, "|", "FEELS", "LIKE", temp, "°"))






# search box
text_field = tk.Entry(screen, justify="center", width = 17, font=("poppins", 25, "bold"), bg = "#404040", fg= "white")
text_field.place(x=50, y=40)

# Set the placeholder text
text_field.insert(0, "Enter City here")

# Bind the <FocusIn> event to a function that will delete the placeholder text
text_field.bind("<FocusIn>", lambda event: text_field.delete(0, "end"))

#search_icon
search_icon = PhotoImage(file="search.png")
search = Button(image= search_icon, borderwidth=0 , cursor="hand2", command=getWeather)
search.place(x =445, y=33)

#logo
logo_image = PhotoImage(file='logo1.png')
logo = Label(image=logo_image)
logo.place(x= 200, y=140)

#time
time = Label(screen, font= ("arial", 15, "bold"))
time.place(x = 30, y =100)
clock = Label(screen, font=("Helevtica", 20))
clock.place(x= 30, y=130)


t = Label(font=("arial", 70, 'bold'), fg = "#ee666d")
t.place(x= 500, y=150)
c = Label(font=("arial", 15, 'bold'))
c.place(x= 500, y= 300)

screen.mainloop()


from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 


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

# search box
text_field = tk.Entry(screen, justify="center", width = 17, font=("poppins", 25, "bold"), bg = "#404040", fg= "white")
text_field.place(x=50, y=40)

# Set the placeholder text
text_field.insert(0, "Enter City here")

# Bind the <FocusIn> event to a function that will delete the placeholder text
text_field.bind("<FocusIn>", lambda event: text_field.delete(0, "end"))

#logo
logo_image = PhotoImage(file='logo1.png')
logo = Label(image=logo_image)
logo.place(x= 150, y=100)

#label
label1 = Label(screen, text="WIND", font=('Helevtica', 15, "bold"), fg ="#1ab5ef")
label1.place(x= 120, y= 400)

label2 = Label(screen, text="HUMIDITY", font=('Helevtica', 15, "bold"), fg ="#1ab5ef")
label2.place(x= 250, y= 400)

label3 = Label(screen, text="DESCRIPTION", font=('Helevtica', 15, "bold"), fg ="#1ab5ef")
label3.place(x= 430, y= 400)

label4 = Label(screen, text="PRESSURE", font=('Helevtica', 15, "bold"), fg ="#1ab5ef")
label4.place(x= 650, y= 400)
screen.mainloop()


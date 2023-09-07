#Quinn Panos        9-7-2023
#Creating a simple weather app

import json
import requests

import tkinter as tk
from tkinter import *

citychoice = input("Enter City Here:")

response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key=APIKEY9&q={citychoice}&days=1&aqi=no&alerts=yes")
#print(response.status_code)
#print(response.json())

location = response.json()['location']["name"]
region = response.json()["location"]["region"]
country = response.json()["location"]["country"]
local_time = response.json()["location"]["localtime"]

temp_f = response.json()["current"]["temp_f"]
temp_fah = str(temp_f)

import tkinter as tk
from tkinter import *

root=tk.Tk() 
root.title("Quinn's Weather App")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#ADD8E6")
tk.Canvas()

Label(root,text=location, width=24, height=1, font=("helvetica",30,"bold"), fg="#000000", bg="#ADD8E6", ).place(x=0,y=10)
Label(root,text=region, width=24, height=1, font=("helvetica",30,"bold"), fg="#000000", bg="#ADD8E6", ).place(x=0,y=125)
Label(root,text=country, width=24, height=1, font=("helvetica",30,"bold"), fg="#000000", bg="#ADD8E6", ).place(x=0,y=250)
Label(root,text=local_time, width=24, height=1, font=("helvetica",30,"bold"), fg="#000000", bg="#ADD8E6", ).place(x=0,y=375)
Label(root,text=temp_fah + "°F", width=24, height=1, font=("helvetica",30,"bold"), fg="#000000", bg="#ADD8E6", ).place(x=0,y=500)

root.mainloop()

from tkinter import *
from tkinter import ttk
import requests

win = Tk()
win.title("Basic Weather App")
win.config(bg="orange")
win.geometry("500x600")

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
    weather_label_1.config(text=data["weather"][0]["main"])
    weather_label_2.config(text=data["weather"][0]["description"])
    temperature = int(data["main"]["temp"] - 273.15)
    Temperature_label_1.config(text=f"{temperature}°C")
    Pressure_label_1.config(text=data["main"]["pressure"])

name_label=Label(win,text="Basic Weather App",font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)


city_name = StringVar()
list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
             "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh","Maharashtra", "Manipur",
             "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
             "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]

com = ttk.Combobox(win,text="Basic Weather App",values=list_name,
                   font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

weather_label=Label(win,text="Weather Climate",font=("Time New Roman",20,))
weather_label.place(x=25,y=260,height=50,width=210)

weather_label_1=Label(win,text="",font=("Time New Roman",20,))
weather_label_1.place(x=250,y=260,height=50,width=210)

weather_label=Label(win,text="Weather Description",font=("Time New Roman",17))
weather_label.place(x=25,y=330,height=50,width=210)

weather_label_2=Label(win,text="",font=("Time New Roman",17))
weather_label_2.place(x=250,y=330,height=50,width=210)

Temperature_label=Label(win,text="Temperature",font=("Time New Roman",17))
Temperature_label.place(x=25,y=400,height=50,width=210)

Temperature_label_1=Label(win,text="",font=("Time New Roman",17))
Temperature_label_1.place(x=250,y=400,height=50,width=210)

Pressure_label=Label(win,text="Pressure",font=("Time New Roman",17))
Pressure_label.place(x=25,y=470,height=50,width=210)

Pressure_label_1=Label(win,text="",font=("Time New Roman",17))
Pressure_label_1.place(x=250,y=470,height=50,width=210)

done_button=Button(win,text="Get Weather",font=("Time New Roman",20),command=data_get)
done_button.place(x=160, y=190, height=50, width=180)

win.mainloop()
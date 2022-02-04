from cgitb import text
import tkinter as tk
from tkinter import *
import requests 
from PIL import Image,ImageTk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
import time
#import TimezoneFinder


root = tk.Tk()  #Create the GUI application main window.

root.title("Weather App")
root.geometry("600x500")


#apikeys = 7f4b6926e804903bbc8ebb70d8727a03
#apiurl = api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}


def getWeather():

    city = txt_box.get()

    geolocator = Nominatim(user_agent = 'geoapiExercises')
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng = location.longitude, lat = location.latitude)
    #print(result)
    
    home = pytz.timezone(result)
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    clock.config(text = curr_clock)
    name.config(text="Current Time")

    #weather
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=7f4b6926e804903bbc8ebb70d8727a03"
    json_data = requests.get(api).json()
    print(json_data)

    wind = json_data['wind']['speed']
    humidity = json_data['main']['humidity']
    des = json_data['weather'][0]['description']
    pres = json_data['main']['pressure']
    
    tempera = int(json_data["main"]["temp"]-273.15)
    condition = json_data['weather'][0]['main']
    
    t.config(text=(tempera,'°'))
    c.config(text=(condition,'|', 'SEASON'))

    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=des)
    p.config(text=pres)

    #weather_key = "7f4b6926e804903bbc8ebb70d8727a03"
    #url = 'https://api.openweathermap.org/data/2.5/weather'
    #params={}
    #response=request.get(url,params)



bg_img = Image.open('./W_window_image.jpg')
bg_img = bg_img.resize((600,500),Image.ANTIALIAS)
bg_img_photo = ImageTk.PhotoImage(bg_img)  #converting the image into PhotoImage

bg_label = tk.Label(root,image=bg_img_photo)
bg_label.place(x=0,y=0,width=600,height=500)

#root.wm_attributes('-transparentcolor', 'white')

txt_box = tk.Entry(bg_label,fg='white',font=('poppins',16,'bold'),justify='center',width=18,bg='#404040')
txt_box.grid(row=0,column=0,sticky='w',)
txt_box.place(x=100,y=60,width=240,height=40)

#btn1 = tk.Button(frame1,text='Weather Search',fg='Dark Blue',font=('times new roman',12,'bold'))
#btn1.grid(row=0,column=0,padx=5)

search_img = Image.open('./search_icon.png')
search_img = search_img.resize((75,35),Image.ANTIALIAS)
search_img_photo = ImageTk.PhotoImage(search_img)  #converting the image into PhotoImage

frame1 = tk.Frame(bg_label, bg = 'Black')
frame1.place(x=350,y=60,width=80,height=40)

search_btn = tk.Button(frame1,image=search_img_photo,command=getWeather)
search_btn.grid(row=0,column=0)

#bottombox
#bottombox_img = Image.open('./bottomlabel.png')
#bottombox_img = bottombox_img.resize((500,80),Image.ANTIALIAS)
#bottombox_img_photo = ImageTk.PhotoImage(bottombox_img)  #converting the image into PhotoImage

#bottombox_label = tk.Label(root,image=bottombox_img_photo)
#bottombox_label.pack(padx=5,pady=5,side=BOTTOM)

#time
name = Label(root,bg='#404040',fg='white',font=('arial',12,'bold'))
name.place(x=65,y=180)

clock = Label(root,bg='Black',fg='white', font=('Helvetica',24))
clock.place(x=50,y=210)     

#Labels

label1 = Label(root,text='WIND',fg='white',font=('Helvetica',12,'bold'),bg='#404040')
label1.place(x=30,y=400)

label2 = Label(root,text='HUMIDITY',fg='white',font=('Helvetica',12,'bold'),bg='#404040')
label2.place(x=130,y=400)

label3 = Label(root,text='DESCRIPTION',fg='white',font=('Helvetica',12,'bold'),bg='#404040')
label3.place(x=320,y=400)

label4 = Label(root,text='PRESSURE',fg='white',font=('Helvetica',12,'bold'),bg='#404040')
label4.place(x=490,y=400)

t = Label(fg='White', bg='#404040',font=('Arial',32,'bold'))
t.place(x=430,y=190)

c = Label(font=('Arial',12,'bold'))
c.place(x=400,y=260)

w = Label(text='...',bg='#404040',font=('Arial',14,'bold'))
w.place(x=30,y=430)

h = Label(text='...',bg='#404040',font=('Arial',14,'bold'))
h.place(x=150,y=430)

d = Label(text='...',bg='#404040',font=('Arial',14,'bold'))
d.place(x=330,y=430)

p = Label(text='...',bg='#404040',font=('Arial',14,'bold'))
p.place(x=520,y=430)

#title = tk.Label(bg_label,text='Current Weather',font=('Arial',24,'bold'),bg='Silver',fg='White')
#title.place(x=80,y=120)

root.mainloop() #main event loop to take action against each event triggered by the user.
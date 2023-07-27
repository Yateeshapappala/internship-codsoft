from tkinter import *
import requests
from tkinter import messagebox

w=Tk()
w.title("Weather forecast Application")
w.geometry("500x500")
name=StringVar()

def weather():
	report.delete("1.0",END)
	api_key="ca2b9ac60a376e75d0719634753766af"
	city=name.get()
	if city:
		url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key
		response=requests.get(url)
		if response.status_code==200:
			data=response.json()
			temp=data["main"]["temp"]
			desc=data["weather"][0]["description"]
			humidity=data["main"]["humidity"]
			min=data["main"]["temp_min"]
			max=data["main"]["temp_max"]
			report.insert(END,city+"\n")
			report.insert(END,"Temperature:"+str(temp)+"K\n")
			report.insert(END,"Description:"+ str(desc)+"\n")
			report.insert(END,"humidity:"+str(humidity)+"\n")
			report.insert(END,"minimum temperature:"+str(min)+"K\n")
			report.insert(END,"max temperature:"+str(max)+"K\n")
		else:
			report.insert(END,"error fetching the data....pls check the city name\n")
	else:
		messagebox.showwarning("Invalid input","Please enter the city name to fetch the data")

	
	name.set("")

    
head=Label(w,text="Weather Forecast",font=("Arial Bold",20))
head.pack(pady=10)

loc_text=Label(w,text="Enter the city name",font=("Arial",15))
loc_text.pack(pady=10)

loc=Entry(w,textvariable=name,font=("Arial",15),relief="solid")
loc.pack(pady=10)

submit=Button(w,text="Submit",command=weather,font=("Arial",15),activebackground="green")
submit.pack(pady=10)

report=Text(w,relief="solid",width=40,font=("Arial",15))
report.pack(pady=10)

w.mainloop()


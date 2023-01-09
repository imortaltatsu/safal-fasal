from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle
def api_call():
    import requests, json
    api_key = "982d13cc7a9a0afd41ec7d1bf3ded48b"
    base_url = "https://history.openweathermap.org/data/2.5/aggregated/month?"
    city_name = "Delhi"
    from datetime import datetime
    date = datetime.now()
    month_number = date.month
    month=str(month_number)
    complete_url = base_url+"month="+month+"&q=" + city_name+"&appid="+api_key
    response = requests.get(complete_url)
    x = response.json()
    global rain,temp
    rain = (x["result"]['precipitation']["mean"])*150
    temp = x["result"]['temp']['mean']-273
    print(x)
    return x
def showw():
    newWindow = Toplevel(frame)
    newWindow.title("RESULT")
    newWindow.geometry("200x200")
    newWindow.configure(background = "#414141")
    water=[232000,252000,248000,283000,219000,231000,282000,245000,283000,279000]
    import random
    windex= random.randrange(0,len(water))
    rain=water[windex] 
    rain=str(rain) 
    str1= "water requred is(in liters):"+rain
    ph=float(entry.get())
    if ph <5.5:
        str2="increase the ph by adding fertilizer"
    elif ph >14:
          str2="ph is invalid"      
    else:
        str2="decrease the ph by adding lime"
    a=ttk.Label(newWindow,text=str1,foreground="#d8eeef")
    b=ttk.Label(newWindow,text=str2,foreground="#d8eeef")
    a.pack()
    b.pack()
def getfromlist(list):
        for i in List.curselection():
                x = (List.get(i))
                return(x[0])
def phpredictor_():
    if ph >5.5:
        return(ph-5.5)
    else:
        return(5.5-ph)
    if rain < 1200:
        water= (1200-rain)
statelist=("Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry")
croplist=["rice","wheat"]
frame = Tk()
frame.title("SAFAL FASAL")
frame.configure(background = "#414141")
frame.protocol("WM_DELETE_WINDOW",frame.destroy)
frame.geometry('450x300')
style = ThemedStyle(frame)
style.set_theme("equilux")
label=ttk.Label(text ="ENTER YOUR PH                                   ",foreground="#d8eeef")
entry=ttk.Entry(foreground="#d8eeef")
ph=entry.get()
label.grid(column= 0,row =0)
entry.grid(column= 1,row =0)
entry1=ttk.Entry(foreground="#d8eeef")
label1=ttk.Label(text ="ENTER YOUR FIELD SIZE IN M SQUARE",foreground="#d8eeef")
label1.grid(column= 0,row =1)
entry1.grid(column= 1,row =1)
fieldsize=entry1.get()
List = Listbox(frame,bg="#414141",fg="#d8eeef")
List.grid(column= 0,row =2)
List1 = Listbox(frame,bg="#414141",fg="#d8eeef")
List1.grid(column= 1,row =2)
sugest= ttk.Button(frame,text ="enter",command=showw)
sugest.grid(column=1,row =3)
advisory=ttk.Label(frame,text ="Ask your agriculture department for ph value of the land",foreground="#d8eeef")
advisory.grid(column=0,row =4)
for i in range(len(statelist)):
    List.insert(i+1,statelist[i])
for i in range(len(croplist)):
    List1.insert(i+1,croplist[i])
frame.mainloop()

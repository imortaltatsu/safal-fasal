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
    print(x)
    return x
de
def showw():
    newWindow = Toplevel(frame)
    newWindow.title("New Window")
    newWindow.geometry("200x200")
def getfromlist(list):
        for i in List.curselection():
                x = (List.get(i))
                return(x[0])
def phpredictor_(ph,water):
    if ph >5.5:
        return(ph-5.5)
    else:
        return(5.5-ph)
def predict(ph,fieldsize):
    x=api_call()
    temp=x['result']['temp']['mean']
    rain=x['result']['precipitation']['mean']
    root = Tk()
    root.title("result")
    root.protocol("WM_DELETE_WINDOW",root.destroy)
    root.geometry('350x300')
statelist=("Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry")
 
frame = Tk()
frame.title("SAFAL FASAL")
frame.protocol("WM_DELETE_WINDOW",frame.destroy)
frame.geometry('350x300')
style = ThemedStyle(frame)
style.set_theme("adapta")
label=ttk.Label(text ="ENTER YOUR PH                                   ")
entry=ttk.Entry()
ph=entry.get()
label.grid(column= 0,row =0)
entry.grid(column= 1,row =0)
entry1=ttk.Entry()
label1=ttk.Label(text ="ENTER YOUR FIELD SIZE IN M SQUARE")
label1.grid(column= 0,row =1)
entry1.grid(column= 1,row =1)
fieldsize=entry1.get()
List = Listbox()
List.grid(column= 0,row =2)
List1 = Listbox()
List1.grid(column= 1,row =2)
sugest= ttk.Button(text ="enter",command=showw)
sugest.grid(column=1,row =3)
frame.mainloop()

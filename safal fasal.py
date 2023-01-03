from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle
def api_call():
    import requests, json
    api_key = "982d13cc7a9a0afd41ec7d1bf3ded48b"
    base_url = "https://history.openweathermap.org/data/2.5/aggregated/month?"
    city_name = "Delhi"
    import datetime
    date = datetime.now()
    month_number = date.month
    month=str(month_number)
    print(complete_url)
    complete_url = base_url+"month="+month+"&q=" + city_name+"&appid="+api_key
    response = requests.get(complete_url)
    x = response.json()
    print(x)
    return x
def getfromlist(list):
        for i in List.curselection():
                x = (List.get(i))
                return(x[0])
def phpredictor_(ph,water):
    if ph >5.5:
        return(ph-5.5)
    else:
        return(5.5-ph)
frame = Tk()
frame.title("SAFAL FASAL")
frame.protocol("WM_DELETE_WINDOW",frame.destroy)
frame.geometry('350x300')
style = ThemedStyle(frame)
style.set_theme("adapta")
label=ttk.Label(text ="ENTER YOUR PH                                   ")
entry=ttk.Entry()
label.grid(column= 0,row =0)
entry.grid(column= 1,row =0)
entry1=ttk.Entry()
label1=ttk.Label(text ="ENTER YOUR FIELD SIZE IN M SQUARE")
label1.grid(column= 0,row =1)
entry1.grid(column= 1,row =1)
List = Listbox()
List.grid(column= 0,row =2)
List1 = Listbox()
List1.grid(column= 1,row =2)
sugest= ttk.Button(text ="enter",command=api_call())
sugest.grid(column=1,row =3)
frame.mainloop()

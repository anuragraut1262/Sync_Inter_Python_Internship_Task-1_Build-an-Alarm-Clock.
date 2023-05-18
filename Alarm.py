
from time import strftime 
from tkinter import * 
import time
import datetime
from pygame import mixer

root = Tk() 
root.title("Alarm Clock")
root.geometry("300x300")
root.resizable(width=False,height=False)

def setalarm():
    alarmtime=f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print(alarmtime)
    if(alarmtime!="::"):
        alarmclock(alarmtime) 

def alarmclock(alarmtime): 
    while True:
        time.sleep(1)
		
        time_now=datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now==alarmtime:
            Wakeup=Label(root, font = ('arial', 15, 'bold'),
            text="Wake up!Wake up",fg="Black").grid(row=9,columnspan=4)
            print("wake up!")
            mixer.init()
            mixer.music.load(r'alarm-clock-short-6402.mp3')
            mixer.music.play()
            break

hrs=StringVar()
mins=StringVar()
secs=StringVar()

Label(root, font = ('arial', 16, 'bold'),
text="Set Your Alarm Clock!\n [ Its 24Hrs Clock ]\n").grid(row=1,columnspan=4)


Label(root, font = ('arial', 11, 'bold'),
text="Hour").grid(row=3,column=1)

hrbtn=Entry(root,textvariable=hrs,width=5,
font =('arial', 18, 'bold')).grid(row=4,column=1)


Label(root, font = ('arial', 11, 'bold'),
text="Minute").grid(row=3,column=2)

minbtn=Entry(root,textvariable=mins,width=5,
font = ('arial', 18, 'bold')).grid(row=4,column=2)

Label(root, font = ('arial', 11, 'bold'),
text="Second").grid(row=3,column=3)

secbtn=Entry(root,textvariable=secs,
width=5,font = ('arial', 18, 'bold')).grid(row=4,column=3)

Label(root, font = ('arial', 10, 'bold'),
text="Welcome").grid(row=7,columnspan=6)

setbtn=Button(root,text="Set Timer!",command=setalarm,bg="#D4AC0D",
fg="Green",font = ('arial', 19, 'bold')).grid(row=8,columnspan=4)

timeleft = Label(root,font=('arial', 20, 'bold')) 
timeleft.grid()
  
mainloop() 

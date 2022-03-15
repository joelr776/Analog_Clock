from doctest import master
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import time
import datetime
window=Tk()

label = Label(window)
label.pack()
 

def clock_update():
        time1 = datetime.datetime.now().strftime("Time: %H:%M:%S")
        label.config(text=time1, bg='#262626', fg='White')
        window.after(1000, clock_update)
        label.place(x=25, y=10)
        
        

clock_update()

window.title(' ')
window.configure(bg='#262626')
window.resizable(width=False, height=False)
window.geometry('150x40')
window.mainloop()

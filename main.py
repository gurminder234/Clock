from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")  # Title of your clock


def time():
    string = strftime('%H:%M:%S %p')  # time format, for 12hr time format change strftime('%H:%M:%S %p') to strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 80), background = "black",foreground = "yellow")  # font,background color,color of digits
label.pack(anchor="center")

time()
mainloop()
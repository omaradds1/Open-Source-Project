import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
import math
window=tk.Tk()
window.title('calculator~gdsc')
frame=tk.Frame(master=window,bg="skyblue",padx=10)
frame.pack()
entry=tk.Entry(master=frame,relief=SUNKEN,borderwidth=3,width=30)
entry.grid(row=0,column=0,columnspan=5,pady=2) 
def welcome():
    print("WELLCOME TO CALCULATOR")
def myclick(number):
    entry.insert(tk.END,number)
def equal():
    try:
        y=str(eval(entry.get()))
        entry.delete(0,tk.END)
        entry.insert(0,y)
    except:
        tkinter.messagebox.showinfo("error","syntax error")
def clear():
    entry.delete(0,tk.END)
def back():
    entry.delete(len(entry.get())-1)
button_1=tk.Button(master=frame,text="1",padx=15,pady=5,width=3,command=lambda:myclick(1))
button_1.grid(row=5,column=1,pady=2)
button_2=tk.Button(master=frame,text="2",padx=15,pady=5,width=3,command=lambda:myclick(2))
button_2.grid(row=5,column=2,pady=2)
button_3=tk.Button(master=frame,text="3",padx=15,pady=5,width=3,command=lambda:myclick(3))
button_3.grid(row=5,column=3,pady=2)
button_4=tk.Button(master=frame,text="4",padx=15,pady=5,width=3,command=lambda:myclick(4))
button_4.grid(row=4,column=1,pady=2)
button_5=tk.Button(master=frame,text="5",padx=15,pady=5,width=3,command=lambda:myclick(5))
button_5.grid(row=4,column=2,pady=2)
button_6=tk.Button(master=frame,text="6",padx=15,pady=5,width=3,command=lambda:myclick(6))
button_6.grid(row=4,column=3,pady=2)

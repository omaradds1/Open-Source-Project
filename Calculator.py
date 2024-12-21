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

from tkinter import *
from tkinter import ttk  # theme of tk
import tkinter as tk
import math

GUI = Tk()
GUI.title('โปรแกรมคำนวณ BMI')
GUI.geometry('500x250')


Label(GUI, text='น้ำหนักตัว (kg.)', font=('Tahoma', 15), fg='black').pack()
L2 = Entry(GUI, width=35)
L2.pack()

Label(GUI, text='ส่วนสูง (cm.)', font=('Tahoma', 15), fg='black').pack()
L3 = Entry(GUI, width=35)
L3.pack()

def get():
    weight = int(L2.get())
    height = int(L3.get())
    BMI = weight/((height/100)**2)
    label.config(text="{:.1f}".format(BMI))


label = Label(GUI, text="BMI", font=('Calibri 15'))
label.pack(pady=20)

Button(GUI, text="คำนวณ", command=get).pack()


# def Button1():
#     value = StringVar()
#     value.set("Enter your weight")
#     entry = Entry(GUI, textvariable=value)
#     entry.pack()


# FB1 = Frame(GUI)
# FB1.place(x=160, y=30)  # กำหนดpositionตามแกน x,y
# B2 = ttk.Button(FB1, text='คำนวณ', command=Button1)
# B2.pack(ipadx=20, ipady=20)


GUI.mainloop()

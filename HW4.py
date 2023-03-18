from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
################################
import csv

data_all = []


def writecsv(datalist):
    with open('data.csv', newline='') as file:
        fr = csv.reader(file)
        first = next(fr)
        if not first:
            with open('data.csv', 'w') as file:
                fw = csv.writer(file)
                fw.writerow(datalist)
        else:
            with open('data.csv', 'a', newline='') as file:
                fw = csv.writer(file)
                fw.writerow(datalist)  # datalist = ['pen', 'pencil', 'eraser']


def readcsv():
    with open('data.csv', newline='') as fileA:
        fr_A = csv.reader(fileA)
        first = next(fr_A)
    if not first:
        messagebox.showinfo('Data', 'ไม่มีข้อมูล!!')
    else:
        with open('data.csv', newline='') as file:
            fr = csv.reader(file)
            data = list(fr)
            for row in data:
                date = row[0]
                name = row[1]
                weight = row[2]
                height = row[3]
                BMI = float(row[4])
                text_f = f'บันทึกวันที่ {date},ชื่อ {name},น้ำหนัก {weight} kg.,ส่วนสูง {height} cm.,BMI: {BMI:.2f}'
                data_all.append(text_f)
            text = ''
            for item in data_all:
                text += f'{item}\n'
            messagebox.showinfo('บันทึกเสร็จสิ้น', text)


############################################

GUI = Tk()
GUI.title('โปรแกรมคำนวณ BMI')
GUI.geometry('500x450')

W = ttk.LabelFrame(GUI, text='น้ำหนักตัว (kg.)')
W.place(x=125, y=50)

We = StringVar()
E1 = ttk.Entry(W, textvariable=We, font=('Tahoma', 15))
E1.pack(padx=10, pady=10)

H = ttk.LabelFrame(GUI, text='ส่วนสูง (cm.)')
H.place(x=125, y=125)

He = StringVar()
E2 = ttk.Entry(H, textvariable=He, font=('Tahoma', 15))
E2.pack(padx=10, pady=10)

label = Label(GUI, text="BMI", font=('Tahoma', 15))
label.pack(pady=20)

L4 = Frame(GUI)  # คล้ายกระดาน
L4.place(x=200, y=340)

B4 = ttk.Button(L4, text='ดูข้อมูล', command=readcsv)
B4.pack(ipadx=10, ipady=10)

################SECTION RIGHT###########################

LF1 = ttk.LabelFrame(GUI, text='คุณชื่ออะไร?')
LF1.place(x=100, y=200)

V_data = StringVar()  # ตัวแปรพิเศษที่ใช้กับข้อความใน GUI
E1 = ttk.Entry(LF1, textvariable=V_data, font=('Tahoma 15', 18))  # ช่องกรอก
E1.pack(pady=10, padx=10)


def Save():
    t = datetime.now().strftime('%d-%m-%Y')
    name = V_data.get()
    weight = int(We.get())
    height = int(He.get())
    BMI = weight / ((height / 100) ** 2)
    label.config(text="{:.1f}".format(BMI))
    text = [t, name, weight, height, BMI]  # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text)
    V_data.set('')  # เคลียร์ข้อมูลที่อยู่ในช่องกรอก
    We.set('')
    He.set('')
    text_m = f'{name} น้ำหนัก {weight} kg.,ส่วนสูง {height} cm.,BMI: {BMI:.2f}'
    messagebox.showinfo('บันทึกเสร็จสิ้น', text_m)


B1 = ttk.Button(LF1, text='บันทึก', command=Save)
B1.pack(ipadx=10, ipady=10)

GUI.mainloop()

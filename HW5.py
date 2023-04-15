"""โจทย์: จงเขียนโปรแกรมอ่านข้อมูลใน score.csv ที่ได้เก็บข้อมูลคะแนน final ของนักศึกษา โดยมีรูปแบบ ID:name:score
เพื่อค้นหาคะแนนของนักศึกษาตามรหัสนักศึกษา และเมื่อค้นหาข้อมูลไม่พบให้แสดง Not Found"""

import csv
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

Student = {}


def search():
    with open(r"C:\Users\User\OneDrive\Desktop\python101\score.csv", newline='') as file:
        data = csv.reader(file)
        next(data)
        for row in data:
            Id = row[0]
            name = row[1]
            score = float(row[2])
            Student[Id] = {'name': name, 'score': score}
        # print(Student)

        id_search = ID_st.get()
        if id_search in Student:
            text_m = f'รหัสนักศึกษา: {id_search}\nชื่อ: {Student[id_search]["name"]}\nคะแนน: {Student[id_search]["score"]} '
            messagebox.showinfo('Data', text_m)
        else:
            messagebox.showinfo('Data', "Not found!!")
        ID_st.set('')


##########################################################################################################################

GUI = Tk()
GUI.title('Score')
GUI.geometry('500x450')

IDop = ttk.LabelFrame(GUI, text='รหัสนักศึกษา:')
IDop.place(x=100, y=100)

ID_st = StringVar()
E1 = ttk.Entry(IDop, textvariable=ID_st, font=('Tahoma', 20))
E1.pack(padx=10, pady=10)

L4 = Frame(GUI)  # คล้ายกระดาน
L4.place(x=208, y=200)

B4 = ttk.Button(L4, text='search', command=search)
B4.pack(ipadx=10, ipady=10)

GUI.mainloop()

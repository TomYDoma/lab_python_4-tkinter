import random
import tkinter as tk
from math import *
from tkinter.ttk import Treeview

import numpy as np
from PIL import ImageTk, Image

box_lab = tk.Tk()
box_lab.title("Какалов Н.С. || Лабораторная работа №7")
box_lab.geometry("400x500")
box_lab.resizable(width=False, height=False)
box_lab["bg"] = "#E0E0E0"

def function_calculation():
    try:
        array = []
        a = float(entry_a.get())
        b = float(entry_b.get())
        N = float(entry_n.get())
        e = float(entry_e.get())

        k = (b - a) / N
        m = 0
        if 0 <= a < 1 and 0 <= b < 1:
            for x in np.arange(b, a, -k):
                count = 0
                for n in range(0, 25):
                    t = (pow(-1, n) * pow(x, n+1)) / (n+1)
                    count += t
                    if fabs(t) < e:
                        break
                m += 1

                ab = (m, x, count)
                array.append(ab)

            newWindow = tk.Toplevel(box_lab)
            # определяем столбцы
            columns = ("n", "x", "y")

            treeview = Treeview(newWindow, columns=columns, show="headings")
            treeview.grid(column=1, row=2)

            # определяем заголовки
            treeview.heading("n", text="N")
            treeview.heading("x", text="X")
            treeview.heading("y", text="Y")

            treeview.column("#1", width=70)
            treeview.column("#2", width=70)
            treeview.column("#3", width=70)

            # добавляем данные
            for i in array:
                treeview.insert(parent='', index='end', values=i)
        else:
            answer_one["text"] = "Значение функции находится в интервале от 0 до 1"
    except:
        answer_one["text"] = "Программа получила \n неправильные входные данные"


frame_lab1 = tk.Frame(box_lab)
frame_lab1["bg"] = "#E0E0E0"

label_one = tk.Label(frame_lab1, text="Вывод таблицы значений функции, \n вычисляемой с помощью ряда Тейлора:", bg="#E0E0E0", font=("Arial", 15))
label_one.grid(column=0, row=0)

image_z1 = Image.open("img/lab6.png")
pil_image = image_z1.resize((300, 50))
frame_lab1.image_z1 = ImageTk.PhotoImage(pil_image)
image_Label_one = tk.Label(frame_lab1, image=frame_lab1.image_z1, bg="#E0E0E0")
image_Label_one.grid(column=0, row=1)

label_a = tk.Label(frame_lab1, text="Ввод a:", bg="#E0E0E0", font=("Arial", 15))
label_a.grid(column=0, row=2)

entry_a = tk.Entry(frame_lab1, font=("Arial", 10))
entry_a.grid(column=0, row=3)

label_b = tk.Label(frame_lab1, text="Ввод b:", bg="#E0E0E0", font=("Arial", 15))
label_b.grid(column=0, row=4)

entry_b = tk.Entry(frame_lab1, font=("Arial", 10))
entry_b.grid(column=0, row=5)

label_e = tk.Label(frame_lab1, text="Ввод e:", bg="#E0E0E0", font=("Arial", 15))
label_e.grid(column=0, row=6)

entry_e = tk.Entry(frame_lab1, font=("Arial", 10))
entry_e.grid(column=0, row=7)

label_n = tk.Label(frame_lab1, text="Ввод n:", bg="#E0E0E0", font=("Arial", 15))
label_n.grid(column=0, row=8)

entry_n = tk.Entry(frame_lab1, font=("Arial", 10))
entry_n.grid(column=0, row=9)


btn_launch = tk.Button(frame_lab1, text="Вычисление", command=function_calculation, bg="#FFFFFF", font=("Arial", 20))
btn_launch.grid(column=0, row=10, pady=5)

answer_one = tk.Label(frame_lab1, bg="#E0E0E0", font=("Arial", 15))
answer_one.grid(column=0, row=11)

frame_lab1.pack()


box_lab.mainloop()
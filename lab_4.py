import tkinter as tk
from math import sqrt
from tkinter.ttk import Treeview

import numpy as np
from PIL import ImageTk, Image

box_lab = tk.Tk()
box_lab.title("Какалов Н.С. || Лабораторная работа №4")
box_lab.geometry("400x500")
box_lab.resizable(width=False, height=False)
box_lab["bg"] = "#E0E0E0"

def function_calculation():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        n = float(entry_n.get())
        array = []
        k = (b - a) / n
        m = 0
        for x in np.arange(b, a - 0.5, -k):
            m += 1
            if x < 0:
                y = -0.5 * x - 3
                ab = (m, x, y)
                array.append(ab)
            elif 0 <= x < 3:
                y = -sqrt(pow(3, 2) - pow(x, 2))
                ab = (m, x, y)
                array.append(ab)
            elif x == 3:
                y = 0
                ab = (m, x, y)
                array.append(ab)
            elif 3 < x <= 6:
                y = sqrt(pow(3, 2) - pow(x - 6, 2))
                ab = (m, x, y)
                array.append(ab)
            elif x > 6:
                y = 0
                ab = (m, x, y)
                array.append(ab)

        box_table = tk.Toplevel(box_lab)
        # определяем столбцы
        columns = ("n", "x", "y")

        treeview = Treeview(box_table, columns=columns, show="headings")
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

    except:
        answer["text"] = "Программа получила \n неправильные входные данные"


frame_lab1 = tk.Frame(box_lab)
frame_lab1["bg"] = "#E0E0E0"

label_one = tk.Label(frame_lab1, text="Вывод таблицы значений функции, \n заданной ее графиком:", bg="#E0E0E0", font=("Arial", 15))
label_one.grid(column=0, row=0)

image_z1 = Image.open("img/lab2.png")
pil_image = image_z1.resize((400, 150))
frame_lab1.image_z1 = ImageTk.PhotoImage(pil_image)
image_Label_one = tk.Label(frame_lab1, image=frame_lab1.image_z1, bg="#E0E0E0")
image_Label_one.grid(column=0, row=1)

label_a = tk.Label(frame_lab1, text="Ввод a:", bg="#E0E0E0", font=("Arial", 15))
label_a.grid(column=0, row=3)

entry_a = tk.Entry(frame_lab1, font=("Arial", 10))
entry_a.grid(column=0, row=4)

label_b = tk.Label(frame_lab1, text="Ввод b:", bg="#E0E0E0", font=("Arial", 15))
label_b.grid(column=0, row=5)

entry_b = tk.Entry(frame_lab1, font=("Arial", 10))
entry_b.grid(column=0, row=6)

label_n = tk.Label(frame_lab1, text="Ввод N:", bg="#E0E0E0", font=("Arial", 15))
label_n.grid(column=0, row=7)

entry_n = tk.Entry(frame_lab1, font=("Arial", 10))
entry_n.grid(column=0, row=8)

btn_launch = tk.Button(frame_lab1, text="Вычисление", command=function_calculation, bg="#FFFFFF", font=("Arial", 20))
btn_launch.grid(column=0, row=9, pady=5)

answer = tk.Label(frame_lab1, bg="#E0E0E0", font=("Arial", 15))
answer.grid(column=0, row=10)


frame_lab1.pack()


box_lab.mainloop()
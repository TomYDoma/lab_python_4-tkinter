import random
import tkinter as tk
from math import *

from PIL import ImageTk, Image

box_lab = tk.Tk()
box_lab.title("Какалов Н.С. || Лабораторная работа №6")
box_lab.geometry("400x500")
box_lab.resizable(width=False, height=False)
box_lab["bg"] = "#E0E0E0"

def function_calculation():
    try:
        x = float(entry_x.get())
        e = float(entry_e.get())
        m = 0
        if 0 <= x < 1:
            for n in range(0, 25):
                t = (pow(-1, n) * pow(x, n+1)) / (n+1)
                if fabs(t) < e:
                    break
                else:
                    m += t
            answer_one["text"] = "Сумма ряда: " + str(m)
        else:
            answer_one["text"] = "Должен лежать в интервале от 0 до 1"
    except:
        answer_one["text"] = "Программа получила \n неправильные входные данные"


frame_lab1 = tk.Frame(box_lab)
frame_lab1["bg"] = "#E0E0E0"

label_one = tk.Label(frame_lab1, text="Вывод таблицы значений функции, \n заданной ее графиком:", bg="#E0E0E0", font=("Arial", 15))
label_one.grid(column=0, row=0)

image_z1 = Image.open("img/lab6.png")
pil_image = image_z1.resize((300, 50))
frame_lab1.image_z1 = ImageTk.PhotoImage(pil_image)
image_Label_one = tk.Label(frame_lab1, image=frame_lab1.image_z1, bg="#E0E0E0")
image_Label_one.grid(column=0, row=1)

label_x = tk.Label(frame_lab1, text="Ввод x:", bg="#E0E0E0", font=("Arial", 15))
label_x.grid(column=0, row=3)

entry_x = tk.Entry(frame_lab1, font=("Arial", 10))
entry_x.grid(column=0, row=4)

label_e = tk.Label(frame_lab1, text="Ввод e (точность):", bg="#E0E0E0", font=("Arial", 15))
label_e.grid(column=0, row=5)

entry_e = tk.Entry(frame_lab1, font=("Arial", 10))
entry_e.grid(column=0, row=6)

btn_launch = tk.Button(frame_lab1, text="Вычисление", command=function_calculation, bg="#FFFFFF", font=("Arial", 20))
btn_launch.grid(column=0, row=9, pady=5)

answer_one = tk.Label(frame_lab1, bg="#E0E0E0", font=("Arial", 15))
answer_one.grid(column=0, row=10)

answer_two = tk.Label(frame_lab1, bg="#E0E0E0", font=("Arial", 15))
answer_two.grid(column=0, row=11)


frame_lab1.pack()


box_lab.mainloop()
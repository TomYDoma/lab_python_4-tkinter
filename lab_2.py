import tkinter as tk
from math import*
from PIL import ImageTk, Image

box_lab = tk.Tk()
box_lab.title("Какалов Н.С. || Лабораторная работа №2")
box_lab.geometry("400x500")
box_lab.resizable(width=False, height=False)
box_lab["bg"] = "#E0E0E0"

def function_calculation():
    try:
        x = float(entry_x.get())
        if x < 0:
            y = -0.5 * x - 3
            answer["text"] = str(y)
        elif 0 <= x < 3:
            y = -sqrt(pow(3, 2) - pow(x, 2))
            answer["text"] = str(round(y, 3))
        elif x == 3:
            y = 0
            answer["text"] = str(y)
        elif 3 < x <= 6:
            y = sqrt(pow(3, 2) - pow(x - 6, 2))
            answer["text"] = str(round(y, 3))
        elif x > 6:
            y = 0
            answer["text"] = str(y)
    except:
        answer["text"] = "Программа получила \n неправильные входные данные"


frame_lab1 = tk.Frame(box_lab)
frame_lab1["bg"] = "#E0E0E0"

label_one = tk.Label(frame_lab1, text="Вычисление значения функции, \n заданной ее графиком:", bg="#E0E0E0", font=("Arial", 15))
label_one.grid(column=0, row=0)

image_z1 = Image.open("img/lab2.png")
pil_image = image_z1.resize((400, 150))
frame_lab1.image_z1 = ImageTk.PhotoImage(pil_image)
image_Label_one = tk.Label(frame_lab1, image=frame_lab1.image_z1, bg="#E0E0E0")
image_Label_one.grid(column=0, row=1)

label_x = tk.Label(frame_lab1, text="Ввод X:", bg="#E0E0E0", font=("Arial", 15))
label_x.grid(column=0, row=3)

entry_x = tk.Entry(frame_lab1, font=("Arial", 10))
entry_x.grid(column=0, row=4, pady=30)

btn_launch = tk.Button(frame_lab1, text="Вычисление", command=function_calculation, bg="#FFFFFF", font=("Arial", 20))
btn_launch.grid(column=0, row=5)

answer = tk.Label(frame_lab1, bg="#E0E0E0", font=("Arial", 15))
answer.grid(column=0, row=6)

label_answer_z2 = tk.Label(frame_lab1, bg="#E0E0E0", font=("Arial", 15))
label_answer_z2.grid(column=0, row=7)

frame_lab1.pack()


box_lab.mainloop()
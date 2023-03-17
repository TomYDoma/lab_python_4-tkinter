import random
import tkinter as tk
from PIL import ImageTk, Image

box_lab = tk.Tk()
box_lab.title("Какалов Н.С. || Лабораторная работа №5")
box_lab.geometry("400x500")
box_lab.resizable(width=False, height=False)
box_lab["bg"] = "#E0E0E0"

def function_calculation():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())
        in_target = 0
        past_target = 0
        for i in range(n):
            x = random.randrange(-r, r)
            y = random.randrange(-r, r)
            if (pow((-r) - x, 2) + y * y <= r * r and x <= 0 and y >= 0) \
                    or ((pow(r - x, 2) + y * y) <= r * r and x >= 0 and y <= 0):
                in_target += 1
            else:
                past_target += 1
        answer_one["text"] = "Количество попаданий: " + str(in_target)
        answer_two["text"] = "Количество промахов: " + str(past_target)
    except:
        answer_one["text"] = "Программа получила \n неправильные входные данные"


frame_lab1 = tk.Frame(box_lab)
frame_lab1["bg"] = "#E0E0E0"

label_one = tk.Label(frame_lab1, text="Вывод таблицы значений функции, \n заданной ее графиком:", bg="#E0E0E0", font=("Arial", 15))
label_one.grid(column=0, row=0)

image_z1 = Image.open("img/lab3.png")
pil_image = image_z1.resize((200, 200))
frame_lab1.image_z1 = ImageTk.PhotoImage(pil_image)
image_Label_one = tk.Label(frame_lab1, image=frame_lab1.image_z1, bg="#E0E0E0")
image_Label_one.grid(column=0, row=1)

label_n = tk.Label(frame_lab1, text="Ввод количество выстрелов:", bg="#E0E0E0", font=("Arial", 15))
label_n.grid(column=0, row=3)

entry_n = tk.Entry(frame_lab1, font=("Arial", 10))
entry_n.grid(column=0, row=4)

label_r = tk.Label(frame_lab1, text="Ввод радиус:", bg="#E0E0E0", font=("Arial", 15))
label_r.grid(column=0, row=5)

entry_r = tk.Entry(frame_lab1, font=("Arial", 10))
entry_r.grid(column=0, row=6)

btn_launch = tk.Button(frame_lab1, text="Вычисление", command=function_calculation, bg="#FFFFFF", font=("Arial", 20))
btn_launch.grid(column=0, row=9, pady=5)

answer_one = tk.Label(frame_lab1, bg="#E0E0E0", font=("Arial", 15))
answer_one.grid(column=0, row=10)

answer_two = tk.Label(frame_lab1, bg="#E0E0E0", font=("Arial", 15))
answer_two.grid(column=0, row=11)


frame_lab1.pack()


box_lab.mainloop()
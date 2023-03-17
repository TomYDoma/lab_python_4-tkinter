import tkinter as tk
from math import*
from PIL import ImageTk, Image


box_lab = tk.Tk()
box_lab.title("Какалов Н.С. || Лабораторная работа №1")
box_lab.geometry("400x500")
box_lab.resizable(width=False, height=False)
box_lab["bg"] = "#E0E0E0"

def function_calculation():
    try:
        a = int(entry_a.get())
        z_1 = (sin(2 * a) + sin(5 * a) - sin(3 * a)) / (cos(a) - cos(3 * a) + cos(5 * a))
        z_2 = tan(3 * a)
        label_answer_z1["text"] = "z1 = " + str(round(z_1, 3))
        label_answer_z2["text"] = "z2 = " + str(round(z_2, 3))
    except:
        label_answer_z1["text"] = "Программа получила \n неправильные входные данные"


frame_lab1 = tk.Frame(box_lab)
frame_lab1["bg"] = "#E0E0E0"

label_one = tk.Label(frame_lab1, text="Вычисление значений выражений:", bg="#E0E0E0", font=("Arial", 15))
label_one.grid(column=0, row=0)

image_z1 = Image.open("img/z1_lab1.png")
pil_image = image_z1.resize((200, 50))
frame_lab1.image_z1 = ImageTk.PhotoImage(pil_image)
image_Label_one = tk.Label(frame_lab1, image=frame_lab1.image_z1, bg="#E0E0E0")
image_Label_one.grid(column=0, row=1)

image_z2 = Image.open("img/z2_lab1.png")
pil_image = image_z2.resize((100, 30))
frame_lab1.image_z2 = ImageTk.PhotoImage(pil_image)
image_Label_two = tk.Label(frame_lab1, image=frame_lab1.image_z2, bg="#E0E0E0")
image_Label_two.grid(column=0, row=2)

label_a = tk.Label(frame_lab1, text="Ввод а:", bg="#E0E0E0", font=("Arial", 15))
label_a.grid(column=0, row=3)

entry_a = tk.Entry(frame_lab1, font=("Arial", 10))
entry_a.grid(column=0, row=4, pady=30)

btn_launch = tk.Button(frame_lab1, text="Вычисление", command=function_calculation, bg="#FFFFFF", font=("Arial", 20))
btn_launch.grid(column=0, row=5)

label_answer_z1 = tk.Label(frame_lab1, bg="#E0E0E0", font=("Arial", 15))
label_answer_z1.grid(column=0, row=6)

label_answer_z2 = tk.Label(frame_lab1, bg="#E0E0E0", font=("Arial", 15))
label_answer_z2.grid(column=0, row=7)

frame_lab1.pack()


box_lab.mainloop()
import tkinter as tk
from PIL import ImageTk, Image

box_lab = tk.Tk()
box_lab.title("Какалов Н.С. || Лабораторная работа №3")
box_lab.geometry("400x500")
box_lab.resizable(width=False, height=False)
box_lab["bg"] = "#E0E0E0"

def function_calculation():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        r = float(entry_r.get())

        if (x * x + y * y <= r * r and -r <= x <= r and 0 <= y <= r) \
                or (y <= x and -r <= x <= 0 and -r <= y <= 0):
            answer["text"] = "Входит"
        else:
            answer["text"] = "Не входит"
    except:
        answer["text"] = "Программа получила \n неправильные входные данные"


frame_lab1 = tk.Frame(box_lab)
frame_lab1["bg"] = "#E0E0E0"

label_one = tk.Label(frame_lab1, text="Проверка принадлежности точки \n заданной области на плоскости:", bg="#E0E0E0", font=("Arial", 15))
label_one.grid(column=0, row=0)

image_z1 = Image.open("img/lab3.png")
pil_image = image_z1.resize((200, 200))
frame_lab1.image_z1 = ImageTk.PhotoImage(pil_image)
image_Label_one = tk.Label(frame_lab1, image=frame_lab1.image_z1, bg="#E0E0E0")
image_Label_one.grid(column=0, row=1)

label_x = tk.Label(frame_lab1, text="Ввод X:", bg="#E0E0E0", font=("Arial", 15))
label_x.grid(column=0, row=3)

entry_x = tk.Entry(frame_lab1, font=("Arial", 10))
entry_x.grid(column=0, row=4)

label_y = tk.Label(frame_lab1, text="Ввод Y:", bg="#E0E0E0", font=("Arial", 15))
label_y.grid(column=0, row=5)

entry_y = tk.Entry(frame_lab1, font=("Arial", 10))
entry_y.grid(column=0, row=6)

label_r = tk.Label(frame_lab1, text="Ввод R:", bg="#E0E0E0", font=("Arial", 15))
label_r.grid(column=0, row=7)

entry_r = tk.Entry(frame_lab1, font=("Arial", 10))
entry_r.grid(column=0, row=8)

btn_launch = tk.Button(frame_lab1, text="Вычисление", command=function_calculation, bg="#FFFFFF", font=("Arial", 20))
btn_launch.grid(column=0, row=9, pady=5)

answer = tk.Label(frame_lab1, bg="#E0E0E0", font=("Arial", 15))
answer.grid(column=0, row=10)


frame_lab1.pack()


box_lab.mainloop()
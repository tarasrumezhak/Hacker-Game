import tkinter
from PIL import Image, ImageTk, ImageSequence
import os
import random
from tkinter import ttk
from check_number import *
import os
import sys

window = tkinter.Tk()
window.wm_iconbitmap(r"icon.ico")
window.title("Hacker Game")
window.resizable(False, False)
canvas = tkinter.Canvas(window, width = 980, height = 690)
canvas.pack()

#Код для гіфки
sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(r"hack1.gif"))]
image = canvas.create_image(500, 370, image = sequence[0])
animating = True
def animate(counter):
    canvas.itemconfig(image, image = sequence[counter])
    if not animating:
        return
    window.after(33, lambda: animate((counter + 1) % len(sequence)))
animate(0)


#Функція туторіалу
def create_window():
    root = tkinter.Toplevel(window)
    root.title("Tutorial")
    img2 = ImageTk.PhotoImage(Image.open(r"tutorial.jpg"))
    panel = tkinter.Label(root, image = img2, compound = tkinter.CENTER)
    widget_tut.destroy()
    panel.pack()
    root.mainloop()

#Функція типів
def create_window_types():
    root = tkinter.Toplevel(window)
    root.title("Numbers Types")
    text = '''The aim of this game is to learn about different sequences of integer numbers, especially about even, happy and Ulam’s numbers.
Even numbers are those integers that are divided by two without any reminders.
Examples:
2 (2 % 2 = 0), 4 (4 % 2 = 0), 72 (72 % 2 = 0), 1016 (1016 % 2 = 0) and so on.
Happy numbers is the sequence of the integers where each element can be represented as the least unique sum of two integers given before.
Examples:
1 (default), 2 (default), 3 (1 + 2 = 3), 4 (1 + 3 = 4), 6 (2 + 4 = 6)*, 8 (2 + 6 = 8), 11 (8 + 3 = 11) and so on.
*5 is omitted, because it can be represented as 2 + 3 and 1 + 4 as well, but we look for unique sums; we also don’t consider combinations
like 2+2 or 3+3 because the integers have to be different
A happy number is defined by the following process: starting with any positive integer, replace the number by the sum of the squares
of its digits in base-ten, and repeat the process until the number either equals 1 (where it will stay), or it loops endlessly in
a cycle that does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers (or sad numbers).
Examples:
1 (1^2 = 1), 7 (7^2 = 49, 4^2 + 9^2 = 97, 9^2 + 7^2 = 130, 1^2 + 3^2 + 0^2 = 10, 1^2 + 0^2 = 1) and so on
    '''
    panel = tkinter.Label(root, text = text, font = "Times 15", compound = tkinter.CENTER)
    panel.pack()
    root.mainloop()

#Функція передісторії
def create_window_hist():
    root = tkinter.Toplevel(window)
    root.title("Prehistory")
    text = '''
It is just a nice Thursday evening. Yesterday you had an amazing tour around Under Defense company,
 so now you are just sitting on your bed and dreaming about great hacker future. But suddenly,
 just as you have been thinking about hacking the Pentagon,
  you realize that tomorrow is Friday. This means: programming test. Sure, you are not ready, who ever was?
“What can I do?” is the only thought in your mind now. There is no doubt tat you have to come up with something cool and easy.
“Of, course! Their correspondence!..”
Surely, the only way to pass your programming test is to hack teacher’s correspondence.
 But it is not an easy task, they are huge fans of integer sequences,
so they use those numbers all the time they need to hide some information or to give student a bad grade on purpose.
But anyway the challenge is accepted!
So you turn your laptop on and here it goes…
Good luck! May the FBI not catch you!
    '''
    panel = tkinter.Label(root,text = text, font = ("MV Boli", 14 ),  compound = tkinter.CENTER)
    widget_tut.destroy()
    panel.pack()
    root.mainloop()


#Кнопка передісторії
button_prehistory = tkinter.Button(window, text="History", command=create_window_hist, bg = "#5F7D8E", fg = "white")
button_prehistory.pack(side = "left")

#Кнопка типів
b = tkinter.Button(window, text="Types", command=create_window_types, bg = "#5F7D8E", fg = "white")
b.pack(side = "left")

#Просто текст опису
text_mes = "Here will be shown some \n intercepted cipher numbers:"
widget1 = tkinter.Label(canvas, background="#466D1D", text=text_mes, font="Helvetica 14 bold")
canvas.create_window(460, 420, window = widget1)

#Генерація випадкових чисел за допомогою кнопки
widget2 = tkinter.Label(canvas, background="green", font="Times 26 bold")
canvas.create_window(700, 420, window = widget2)
def set_numb():
    def create_window_err2():
        set_secs_err = tkinter.Toplevel(window)
        set_secs_err.title("WARNING!")
        text = "Please set the positive range number in the input field"
        err_mes = tkinter.Label(set_secs_err, text = text , font=("Helvetica", 16),  fg="red",  compound = tkinter.CENTER)
        err_mes.pack()
    try:
        if third_entry.get() and int(third_entry.get()) > 0:
            text_num = random.choice([x for x in range(1, int(third_entry.get()) + 1)])
            widget2.__setitem__("text", text_num)
            pb["value"] = 100
            set_secs()
            button3["state"] = "disabled"
            button_u["state"] = "normal"
            button_e["state"] = "normal"
            button_h["state"] = "normal"
            button_o["state"] = "normal"
        else:
                create_window_err2()
    except ValueError:
        create_window_err2()

button3 = tkinter.Button(window, text="Set Number", command = set_numb, bg = "#5F7D8E", fg = "white")
button3.pack(side="left")

#Там де пише хакання електронних адрес
widget3 = tkinter.Label(window, background="#028A0F", font="Times 14 bold", width = 42)
canvas.create_window(545, 706, window = widget3)
def hacking_wind():
    text_hack = "{:35}".format(" TERMINAL: >>> hacking " + random.choice(["rumezhak", "dubei", "kmet", "romaniuk", "dobosevych", "garkot", "lenio"]) + "@ucu.edu.ua")
    widget3.__setitem__("text", text_hack)
    window.after(150, hacking_wind)

#Поле, де виводиться отриманий код
entry_label = tkinter.Label(canvas)
canvas.create_window(150, 40, window = entry_label)
entry1 = tkinter.Entry(entry_label, text = "Hello", bg = "#710C04", width = 20, font = "Times 20 bold", foreground = "yellow")
entry1.pack()

#Вікно, яке вискакує, коли програв
def lose():
    lose_wind = tkinter.Label(canvas, text = "You lose", background ="green",  font="Times 60 bold")
    canvas.create_window(545, 300, window = lose_wind)
    window.destroy()
    root = tkinter.Tk()
    root.title("Danger")
    root.wm_iconbitmap(r"fbi.ico")
    photo = tkinter.PhotoImage(file = r"security.png")
    text = "FBI detected you, run awaaaaaaaay"
    label = tkinter.Label(root, image = photo)
    label2 = tkinter.Label(root, text = text, font = "Broadway 16", fg = "red")
    label.pack()
    label2.pack()
    root.mainloop()


#Шифр повідомлення
cipher = "C@AG6nQ$AX%3_[4)"
cipher_index = 0

def control():
    '''
    Вставляє шифр в поле
    '''
    try:
        if pb["value"] > 0:
            set_numb()
            global cipher_index
            global cipher
            entry1.insert(0, cipher[::-1][cipher_index])
            cipher_index += 1
            pb["value"] = 100
            set_secs()
    except IndexError:
        button1["state"] = "normal"
        pb.destroy()


def even_control():
    if is_even(widget2.__getitem__("text")):
        control()
    else:
        lose()
def happy_control():
    if is_happy(widget2.__getitem__("text")):
        control()
    else:
        lose()
def ulam_control():
    if ulam_n(widget2.__getitem__("text")):
        control()
    else:
        lose()
def none_control():
    if not is_even(widget2.__getitem__("text")) and not is_happy(widget2.__getitem__("text")) and not ulam_n(widget2.__getitem__("text")):
        control()
    else:
        lose()

#Кнопка для парних чисел
widget4 = tkinter.Label(canvas)
canvas.create_window(700, 500, window = widget4)
button_e = tkinter.Button(widget4, text=">EVEN<", command = even_control, font = ("Bauhaus 93", 12), bg = "green", width = 9, state = "disabled")
button_e.pack()

#Кнопка для щасливих чисел
widget4 = tkinter.Label(canvas)
canvas.create_window(700, 550, window = widget4)
button_h = tkinter.Button(widget4, text=">HAPPY<", command = happy_control, font = ("Bauhaus 93", 12), bg = "green", width = 9, state = "disabled")
button_h.pack()

#Кнопка для чисел Улама
widget4 = tkinter.Label(canvas)
canvas.create_window(700, 600, window = widget4)
button_u = tkinter.Button(widget4, text=">ULAM<", command = ulam_control, font = ("Bauhaus 93", 12), bg = "green", width = 9, state = "disabled")
button_u.pack()

#Кнопка для всіх інших чисел
widget4 = tkinter.Label(canvas)
canvas.create_window(700, 650, window = widget4)
button_o = tkinter.Button(widget4, text=">OTHER<", command = none_control, font = ("Bauhaus 93", 12), bg = "green", width = 9, state = "disabled")
button_o.pack()

widget_pb = tkinter.Label(canvas)
canvas.create_window(640, 370, window = widget_pb)
pb = ttk.Progressbar(widget_pb, orient ="horizontal", length = 200, mode ="determinate")
pb.pack()
pb["maximum"] = 100
pb["value"] = 100
def progress(a):
    if pb["value"] > 0:
        pb.__setitem__("value", pb["value"] - 1)
    window.after(a, lambda: progress(a))
    if pb["value"] == 0:
        lose()

#Поле для введення секуунд
seconds_entry = tkinter.Entry(window, bg = "white")
seconds_entry.pack(side = "right")

button_range = tkinter.Button(text = "Range>>>", bg = "#5F7D8E", fg = "white")
button_range.pack(side = "left")

#Поле для введення діапазону
third_entry = tkinter.Entry(window, bg = "white", width = 12)
third_entry.pack(side = "left")
def set_secs():
    def create_window_err():
        set_secs_err = tkinter.Toplevel(window)
        set_secs_err.title("WARNING!")
        text = "Please set the positive seconds number in the input field"
        err_mes = tkinter.Label(set_secs_err, text = text , font=("Helvetica", 16),  fg="red",  compound = tkinter.CENTER)
        err_mes.pack()
    try:
        if seconds_entry.get() and int(seconds_entry.get()) > 0 :
                secs = seconds_entry.get()
                progress(int(secs) * 10)
        else:
            create_window_err()
    except ValueError:
        create_window_err()


button_sec = tkinter.Button(window, text="Seconds>>>", bg = "#5F7D8E", fg = "white")
button_sec.pack(side = "right")


def create_window_win():
    if entry1.get() == cipher:
        win = tkinter.Toplevel(window)
        win.title("Hacking Done")
        win.title("Done")
        text = "Hacked message >>> \n Hey you, don't you forget that you are using WIFI-UCU??? \n we controll everything here \n STOP doing that!!!"
        mes = tkinter.Label(win, text = text, font=("Helvetica", 16),  fg="red",  compound = tkinter.CENTER)
        mes.pack()

widget_win = tkinter.Label(canvas)
canvas.create_window(150, 80, window = widget_win)
button1 = tkinter.Button(widget_win, text = "DECRYPT", command = create_window_win, background = "#710C04", state = "disable", foreground = "yellow")
button1.pack()


def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)
widget_restart = tkinter.Label(canvas)
canvas.create_window(925, 40, window = widget_restart)
button_restart = tkinter.Button(widget_restart, text = "RESTART", fg = "red", command = restart, bg = "yellow", font = ("Courier", 14))
button_restart.pack()

widget_tut = tkinter.Label(canvas)
canvas.create_window(540, 180, window = widget_tut)
button_tut = tkinter.Button(widget_tut, text = "Tutorial", fg = "red", command = create_window, bg = "yellow", font = ("Courier", 30))
button_tut.pack()

window.after(150, hacking_wind)
window.mainloop()

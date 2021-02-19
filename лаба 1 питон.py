import tkinter as T
from tkinter import messagebox

lis = ["-", "."]
n = 5

# p=1 из 9 в 10
# p=2 из 10 в 9


def one_translate(inp):  # перевод
    res = ""
    try:
        inp = float(inp)
        inp = str(inp)
    except:
        if inp != "" and inp not in lis:
            if is_warnings.get() != 1:
                messagebox.showerror("InError", "Please input one number")
        resalt_string.set("Input one number")
    else:
        dub = 0.0
        num = 0
        if "." in inp:
            num = int(inp[0:inp.find(".")])
            dub += float(inp[inp.find("."):len(inp)])
        minus = False
        if num < 0:
            num = num*-1
            minus = True
        while num >= 9:
            res += str(num % 9)
            num = num//9
        res += str(num)
        y = ""
        j = 0
        if dub != 0:
            while j != n:
                dub = dub*9
                dub = str(dub)
                y += str(dub[0:dub.find(".")])
                dub = dub[dub.find("."):len(dub)]
                dub = float(dub)
                j += 1
            ss = res[::-1]+"."+y
        else:
            ss = res[::-1]+"."+"0"
        if minus:

            resalt_string.set("-"+str(ss))
        else:
            resalt_string.set(str(ss))


def second_translate(inp):
    res = 0
    try:
        inp = float(inp)
        inp = str(inp)
    except:
        if inp != "" and inp not in lis:
            if is_warnings.get() != 1:
                messagebox.showerror("InError", "Please input one number")
        resalt_string.set("Input one number")
    else:
        dub = 0.0
        num = 0
        if "." in inp:
            num = int(inp[0:inp.find(".")])
            dub += float(inp[inp.find("."):len(inp)])
        minus = False
        if num < 0:
            num = num*-1
            minus = True
        i = 0
        while num >= 1:
            k = num % (10*(i+1))
            res += k*(9**i)
            num = num//(10*(i+1))
            i += 1
        y = 0.0
        j = -1
        i = 0
        if dub != 0:
            dub = str(dub)
            dub = dub[::-1]
            dub = float(dub)
            while abs(j) != n:
                k = dub % (10*(i+1))
                y += k*(9**j)
                dub = dub//(10*(i+1))
                j -= 1
                i += 1
            ss = res+y
            ss = round(ss, 5)
        else:
            ss = float(res)
        if minus:
            resalt_string.set("-"+str(ss))
        else:
            resalt_string.set(str(ss))


def change1():  # событие из 9 в 10
    global p
    p = 1
    info_string.set("Conversion from {0} to {1}".format(9, 10))


def change2():  # событие из 10 в 9
    global p
    p = 2
    info_string.set("Conversion from {0} to {1}".format(10, 9))

# событие перевода


def converse():
    global p
    if p == 0:

        if is_warnings.get() != 1:
            messagebox.showwarning("Warning", "choose way")
    if p == 1:
        second_translate(main_string.get())
    if p == 2:
        one_translate(main_string.get())


def fun1(event):
    global p
    if p == 1:
        second_translate(main_string.get())
    if p == 2:
        one_translate(main_string.get())


def fun(event):
    if p == 1:
        messagebox.showerror("InError", "You can't input 9 in 9th sistem")
        uss = main_string.get()
        main_string.set(uss[:len(uss)-1])
        resalt_string.set("try again")
    if p == 2:
        one_translate(main_string.get())


def clavia(a):
    if a != -1:
        if p == 1 and a == 9:
            messagebox.showerror("InError", "You can't input 9 in 9th sistem")
        else:
            main_string.set(main_string.get()+str(a))
    else:
        if main_string.get()[0] != "-":
            main_string.set("-"+main_string.get())
        else:
            main_string.set(main_string.get()[1:])


def C1(a):  # событие очистки строк

    if a == 1:
        main_string.set("")
    if a == 2:
        resalt_string.set("")
    if a == 3:
        resalt_string.set("")
        main_string.set("")


def prog_info():
    messagebox.showinfo("About programm", """Лабараторная 1 является
переводчиком из десятичной системы в девятеричную и обратно.
    """)


def author_info():
    messagebox.showinfo("About author", """Разработано студентом группы ИУ7-23Б 
Калашниковым Сергеем
    """)


def C2(nh):
    global n
    n = nh


p = 0
window = T.Tk()


main_string = T.StringVar()
main_string.set("")
resalt_string = T.StringVar()
resalt_string.set("")
info_string = T.StringVar()
info_string.set("Choose metode")
is_warnings = T.IntVar()

# Меню окна
main_menu = T.Menu()  # Главное меню
dop_menu = T.Menu()  # Меню выбора режима
dop_clean = T.Menu()  # Меню очистки
dop_info = T.Menu()  # Меню информации

# Меню очистки
dop_clean.add_command(label="Input", command=lambda: C1(1))
dop_clean.add_command(label="Output", command=lambda: C1(2))
dop_clean.add_command(label="All", command=lambda: C1(3))

# Меню выбора режима
dop_menu.add_radiobutton(label="From 9x", command=change1)  # из 9 в 10
dop_menu.add_radiobutton(label="From 10x", command=change2)  # из 10 в 9

# Меню информации
dop_info.add_command(label="About programm", command=prog_info)
dop_info.add_command(label="About author", command=author_info)

# Главное меню
main_menu.add_cascade(label="Conversion", menu=dop_menu)
main_menu.add_cascade(label="Clean", menu=dop_clean)
main_menu.add_cascade(label="Information", menu=dop_info)

# Элементы окна
# чекбокс
is_warningbox = T.Checkbutton(
    text="Don't show warning messages", variable=is_warnings)
is_warningbox.grid(column=3, row=2)

# информационная строка: ввод
kkk = "Enter the number:"

label1 = T.Label(window, text=kkk)
label1.grid(column=1, row=1)

# информационная строка: вывод
kk = "Result:"
label4 = T.Label(window, text=kk)
label4.grid(column=1, row=2, sticky="E")

# информационная строка: режим калькулятора
label3 = T.Label(window, textvariable=info_string)
label3.grid(column=2, row=0)

# строка вывода
label2 = T.Label(window, textvariable=resalt_string)
label2.grid(column=2, row=2)

# текстовое поле для ввода
text = T.Entry(window, width=20, textvariable=main_string)
text.grid(column=2, row=1)
text.bind("<KeyRelease-9>", fun)
text.bind("<KeyRelease>", fun1)

# кнопка перевода


wi = 6
he = 3
start1 = 60
start2 = 90
btn = T.Button(window, text="Convert", command=converse,
               width=wi, height=he, bg="#FF0000", fg="#000")
btn.place(x=start1+wi*2*11, y=start2+he*3*25)
btn1 = T.Button(window, text="1", width=wi,
                height=he, command=lambda: clavia(1), bg="#000", fg="#FFF")
btn1.place(x=start1, y=start2)
btn2 = T.Button(window, text="2", width=wi,
                height=he, command=lambda: clavia(2), bg="#000", fg="#FFF")
btn2.place(x=start1+wi*11, y=start2)
btn3 = T.Button(window, text="3", width=wi,
                height=he, command=lambda: clavia(3), bg="#000", fg="#FFF")
btn3.place(x=start1+wi*2*11, y=start2)
btn4 = T.Button(window, text="4", width=wi,
                height=he, command=lambda: clavia(4), bg="#000", fg="#FFF")
btn4.place(x=start1, y=start2+he*25)
btn5 = T.Button(window, text="5", width=wi,
                height=he, command=lambda: clavia(5), bg="#000", fg="#FFF")
btn5.place(x=start1+wi*11, y=start2+he*25)
btn6 = T.Button(window, text="6", width=wi,
                height=he, command=lambda: clavia(6), bg="#000", fg="#FFF")
btn6.place(x=start1+wi*2*11, y=start2+he*25)
btn7 = T.Button(window, text="7", width=wi,
                height=he, command=lambda: clavia(7), bg="#000", fg="#FFF")
btn7.place(x=start1, y=start2+he*2*25)
btn8 = T.Button(window, text="8", width=wi,
                height=he, command=lambda: clavia(8), bg="#000", fg="#FFF")
btn8.place(x=start1+wi*11, y=start2+he*2*25)
btn9 = T.Button(window, text="9", width=wi,
                height=he, command=lambda: clavia(9), bg="#000", fg="#FFF")
btn9.place(x=start1+wi*2*11, y=start2+he*2*25)
btn0 = T.Button(window, text="0", width=wi,
                height=he, command=lambda: clavia(0), bg="#000", fg="#FFF")
btn0.place(x=start1+wi*11, y=start2+he*3*25)
btn_minus = T.Button(window, text="-", width=wi,
                     height=he, command=lambda: clavia(-1), bg="#FFC000", fg="#000")
btn_minus.place(x=start1, y=start2+he*3*25)

# Создание окна
window.config(menu=main_menu)
window.title("Conversion from 10x to 9x")
window.geometry("500x400")
window.mainloop()

import tkinter as T
from tkinter import messagebox

lis=["-","."]

#p=1 из 9 в 10
#p=2 из 10 в 9
def one_translate(inp):#перевод
    res=""
    try:
        inp=float(inp)
        inp=str(inp)
    except:
        if inp!="" and inp not in lis:
            messagebox.showerror("InError","Please input one number")
        resalt_string.set("Input one number")
    else:
        dub=0.0
        num=0
        if "." in inp:
            num=int(inp[0:inp.find(".")])
            dub+=float(inp[inp.find("."):len(inp)])
        minus=False
        if num<0:
            num=num*-1
            minus=True
        while num>=9:
            res+=str(num%9)
            num=num//9
        res+=str(num)
        y=""
        j=0
        while j!=10:
            dub=dub*9
            dub=str(dub)
            y+=str(dub[0:dub.find(".")])
            dub=dub[dub.find("."):len(dub)]
            dub=float(dub)
            j+=1
        if minus:
            resalt_string.set("-"+res[::-1]+"."+y)
        else:
            resalt_string.set(res[::-1]+"."+y)

def second_translate(num):
    res=0
    try:
        num=int(num)
    except:
        if num!="" and num not in lis:
            messagebox.showerror("InError","Please input one number")
        resalt_string.set("Input one number")
    else:
        minus=False
        if num<0:
            num=num*-1
            minus=True
        i=0
        while num>=1:
            k=num%(10*(i+1))
            res+=k*(9**i)
            num=num//(10*(i+1))
            i+=1
        if minus:
            resalt_string.set("-"+str(res))
        else:
            resalt_string.set(str(res))

def change1():#событие из 9 в 10
    global p
    p=1
    info_string.set("Conversion from {0} to {1}".format(9,10))
    
def change2():#событие из 10 в 9
    global p
    p=2
    info_string.set("Conversion from {0} to {1}".format(10,9))
    
#событие перевода
def converse():
    global p
    if p==0:
        messagebox.showwarning("Warning","choose way")    
    if p==1:
        second_translate(main_string.get())
    if p==2:
        one_translate(main_string.get())
        
def fun1(event):
    global p
    if p==1:
        second_translate(main_string.get())
    if p==2:
        one_translate(main_string.get())

def fun(event):
    if p==1:
        messagebox.showerror("InError","You can't input 9 in 9th sistem")
        uss=main_string.get()
        main_string.set(uss[:len(uss)-1])
        print(main_string.get())
    if p==2:
        one_translate(main_string.get())


def C1(a):# событие очистки строк 
    
    if a==1:
        main_string.set("")
    if a==2:
        resalt_string.set("")
    if a==3:
        resalt_string.set("")
        main_string.set("")

def prog_info():
    messagebox.showinfo("About programm","""Лабараторная 1 является
переводчиком из десятичной системы в девятеричную и обратно.
    """)

def author_info():
    messagebox.showinfo("About author","""Разработано Калашниковым Сергеем
из группы ИУ7-23Б 
    """)
 

p=0
window = T.Tk()


main_string=T.StringVar()
main_string.set("")
resalt_string=T.StringVar()
resalt_string.set(str(p))
info_string=T.StringVar()
info_string.set("Choose metode")

#Меню окна

main_menu = T.Menu()#Главное меню
dop_menu=T.Menu()#Меню выбора режима
dop_clean=T.Menu()#Меню очистки
dop_info=T.Menu()#Меню информации
dop_dop_info=T.Menu()#

#Меню очистки
dop_clean.add_command(label="Input",command=lambda: C1(1))
dop_clean.add_command(label="Output",command=lambda: C1(2))
dop_clean.add_command(label="All",command=lambda: C1(3))

#Меню выбора режима
dop_menu.add_radiobutton(label="From 9x",command=change1)#из 9 в 10
dop_menu.add_radiobutton(label="From 10x",command=change2)#из 10 в 9

#Меню информации
dop_info.add_command(label="About programm",command=prog_info)
dop_info.add_command(label="About author",command=author_info)

#Главное меню
main_menu.add_cascade(label="Conversion", menu=dop_menu)
main_menu.add_cascade(label="Clean",menu=dop_clean)
main_menu.add_cascade(label="Information",menu=dop_info)

#Элементы окна
#информационная строка: ввод 
kkk="Enter the number:"
label1 = T.Label(window,text=kkk)
label1.grid(column=1,row=1)

#информационная строка: вывод
kk="Result:"
label4 = T.Label(window,text=kk)
label4.grid(column=1,row=2)

#информационная строка: режим калькулятора
label3 = T.Label(window,textvariable=info_string)
label3.grid(column=2,row=0)

#строка вывода
label2 = T.Label(window,textvariable=resalt_string)
label2.grid(column=2,row=2)

#текстовое поле для ввода
text = T.Entry(window,width=20,textvariable=main_string) 
text.grid(column=2, row=1)
text.bind("<KeyRelease-9>", fun)
text.bind("<KeyRelease>", fun1)

#кнопка перевода
btn = T.Button(window,text="Convert",command=converse)
btn.grid(column=3,row=1)
window.config(menu=main_menu)

#Создание окна
window.title("Conversion from 10x to 9x")
window.geometry("500x400")
window.mainloop()

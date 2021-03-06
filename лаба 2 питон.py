import tkinter as T
from tkinter import messagebox
import random


def combsort(alist):
    alen = len(alist)
    gap = (alen * 10 // 13) if alen > 1 else 0
    while gap:
        if 8 < gap < 11:
            gap = 11
        swapped = False
        for i in range(alen - gap):
            if alist[i + gap] < alist[i]:
                alist[i], alist[i + gap] = alist[i + gap], alist[i]
                swapped = True
        gap = (gap * 10 // 13) or swapped
    return alist


def create(N):
    l = []
    for i in range(N):
        l.append(random.randint(-1*N, N))
    print(l)


def converse1():
    l = list_str.get().split(" ")
    if len(l) == 1 and l[0] == "":
        resalt_string.set("Vvedite number")
    else:
        i = 0
        while i < len(l):
            try:
                float(l[i])
            except:
                l.pop(i)
                i -= 2
            i += 1
        resalt_string.set(combsort(l))

def converse():
    return 0


def translate(event):
    print(event.keycode)
    if event.keycode != 32 and event.keycode != 109:
        if event.keycode > 105 or event.keycode < 96:
            #messagebox.showerror("InError", "You can't input letters or sighns")
            uss = list_str.get()
            list_str.set(uss[:len(uss)-1])
            resalt_string.set("try again")
        else:
            resalt_string.set(list_str.get())
    else:
        resalt_string.set(list_str.get())


window = T.Tk()


list_str = T.StringVar()
list_str.set("")
# строка результата
resalt_string = T.StringVar()
resalt_string.set("")
N1 = T.IntVar()
N2 = T.IntVar()
N3 = T.IntVar()


label_i1 = T.Label(window, text="Input array:")
label_i1.grid(column=0, row=0)

label_i2 = T.Label(window, text="Resalt:")
label_i2.grid(column=0, row=1)

label2 = T.Label(window, textvariable=resalt_string)
label2.grid(column=1, row=1)

label_i3 = T.Label(window, text="N1:")
label_i3.grid(column=0, row=2)
label_i4 = T.Label(window, text="N2:")
label_i4.grid(column=0, row=3)
label_i5 = T.Label(window, text="N3:")
label_i5.grid(column=0, row=4)

# text N's
text1 = T.Entry(window, width=20, textvariable=N1)
text1.grid(column=1, row=2)
text2 = T.Entry(window, width=20, textvariable=N2)
text2.grid(column=1, row=3)
text3 = T.Entry(window, width=20, textvariable=N3)
text3.grid(column=1, row=4)


text = T.Entry(window, width=20, textvariable=list_str)
text.grid(column=1, row=0)
text.bind("<KeyRelease>", translate)

# translate
btn = T.Button(window, text="Convert", command=converse,
               bg="#FF0000", fg="#000")
btn.grid(column=3, row=3)

btn1 = T.Button(window, text="Convert1", command=converse1,
               bg="#FF0000", fg="#000")
btn1.grid(column=3, row=0)


window.title("Sort")
window.geometry("500x400")
window.mainloop()

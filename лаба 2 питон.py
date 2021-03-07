import tkinter as T
from tkinter import messagebox
import random
import time


def combsort(alist):
    start = time.time()
    alen = len(alist)
    k = 1.3
    if alen > 1:
        gap = alen//k
    else:
        gap = 0
    while gap:
        if 8 < gap < 11:
            gap = 11
        swapped = False
        for i in range(alen - int(gap)):
            if alist[i + int(gap)] < alist[i]:
                alist[i], alist[i + int(gap)] = alist[i + int(gap)], alist[i]
                swapped = True
        gap = (gap * 10 // 13) or swapped
    stop = time.time()
    return alist, stop - start


def create(N):
    l = []
    i = 0
    for i in range(N):
        l.append(random.randint(-1*N, N))
    return l


def converse():
    l = create(N1.get())
    print(l)
    l = combsort(l)
    T11.set(l[1])
    print(l[0])
    l = combsort(l[0])
    T12.set(l[1])
    print(l[0][::-1])
    l = combsort(l[0][::-1])
    T13.set(l[1])

    l = create(N2.get())
    print(l)
    l = combsort(l)
    T21.set(l[1])
    print(l[0])
    l = combsort(l[0])
    T22.set(l[1])
    print(l[0][::-1])
    l = combsort(l[0][::-1])
    T23.set(l[1])

    l = create(N3.get())
    print(l)
    l = combsort(l)
    T31.set(l[1])
    print(l[0])
    l = combsort(l[0])
    T32.set(l[1])
    print(l[0][::-1])
    l = combsort(l[0][::-1])
    T33.set(l[1])


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
        resalt_string.set(combsort(l)[0])


def translate(event):
    print(event.keycode)
    if event.keycode != 32 and event.keycode != 109:
        if event.keycode > 105 or event.keycode < 96:
            messagebox.showerror(
                "InError", "You can't input letters or sighns")
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

T11 = T.DoubleVar()
T11.set(0)
T12 = T.DoubleVar()
T12.set(0)
T13 = T.DoubleVar()
T13.set(0)
T21 = T.DoubleVar()
T21.set(0)
T22 = T.DoubleVar()
T22.set(0)
T23 = T.DoubleVar()
T23.set(0)
T31 = T.DoubleVar()
T31.set(0)
T32 = T.DoubleVar()
T32.set(0)
T33 = T.DoubleVar()
T33.set(0)

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

label_i31 = T.Label(window, text="N1")
label_i31.grid(column=1, row=5)
label_i41 = T.Label(window, text="N2")
label_i41.grid(column=2, row=5)
label_i51 = T.Label(window, text="N3")
label_i51.grid(column=3, row=5)

label_r1 = T.Label(window, textvariable=T11)
label_r1.grid(column=1, row=6)
label_r2 = T.Label(window, textvariable=T12)
label_r2.grid(column=1, row=7)
label_r3 = T.Label(window, textvariable=T13)
label_r3.grid(column=1, row=8)
label_r4 = T.Label(window, textvariable=T21)
label_r4.grid(column=2, row=6)
label_r5 = T.Label(window, textvariable=T22)
label_r5.grid(column=2, row=7)
label_r6 = T.Label(window, textvariable=T23)
label_r6.grid(column=2, row=8)
label_r7 = T.Label(window, textvariable=T31)
label_r7.grid(column=3, row=6)
label_r8 = T.Label(window, textvariable=T32)
label_r8.grid(column=3, row=7)
label_r9 = T.Label(window, textvariable=T33)
label_r9.grid(column=3, row=8)


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

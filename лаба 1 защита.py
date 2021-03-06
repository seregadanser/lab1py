import tkinter as T

dic={".":".","0":"000","1":"001","2":"010","3":"011","4":"100","5":"101","6":"110","7":"111"}
dic1={"0000":"0","0001":"1","0010":"2","0011":"3","0100":"4",
      "0101":"5","0110":"6","0111":"7","1000":"8","1001":"9",
      "1010":"A","1011":"B","1100":"C","1101":"D","1110":"E",
      "1111":"F",}
def to_h(stre):
    resalt_string.set("")
    fg=""
    for i in range(len(stre)):
        fg+=dic[stre[i]]
    
    if "." in fg:
        fg1=fg[0:fg.find(".")]
        fg2=fg[fg.find(".")+1:len(fg)]
        k =len(fg1)
        if k%4!=0:
            while len(fg1)%4 != 0:
                fg1="0"+fg1
        print(fg1)
        for i in range(0,len(fg1),4):
            if fg1[i:i+4]=="0000" and i==0:
                continue
            else:
                resalt_string.set(resalt_string.get()+dic1[fg1[i:i+4]])
        resalt_string.set(resalt_string.get()+".")
        k =len(fg2)
        if k%4!=0:
            while len(fg2)%4 != 0:
                fg2=fg2+"0"
        print(fg2)
        for i in range(0,len(fg2),4):
            if fg2[i:i+4]=="0000" and i==0:
                continue
            else:
                resalt_string.set(resalt_string.get()+dic1[fg2[i:i+4]])
    else:
        k =len(fg)
        if k%4!=0:
            while len(fg)%4 != 0:
                fg="0"+fg
        print(fg)
        for i in range(0,len(fg),4):
            if fg[i:i+4]=="0000" and i==0:
                continue
            else:
                resalt_string.set(resalt_string.get()+dic1[fg[i:i+4]])

            
    

def translate():
    print(to_when.get())

def fun1(event):#обработка клавиш с клавитуры
    if to_when.get() == 0:
        to_e(main_string.get())
    if to_when.get() == 1:
        to_h(main_string.get())



dict1={}

window = T.Tk()

to_when=T.IntVar()

main_string = T.StringVar()
main_string.set("")
resalt_string = T.StringVar()
resalt_string.set("")

btn = T.Button(window, text="Convert",command=translate)  
btn.grid(column=1,row=0)

where = T.Checkbutton(
    text="translate", variable=to_when)
where.grid(column=1, row=1)

text = T.Entry(window, width=20, textvariable=main_string)
text.grid(column=0, row=0)
text.bind("<KeyRelease>", fun1)

label2 = T.Label(window, textvariable=resalt_string)
label2.grid(column=0, row=1)

window.title("from 8x to 16x")
window.geometry("500x400")
window.mainloop()

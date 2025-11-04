# Лабораторная работа №3 — вариант 8
# Студент: Чэнь Бохань
# Номер студента: 504718

import random
from tkinter import messagebox
import tkinter as tk
def random_pick1():
    words=[]
    global allin
    with open('number.txt','r')as word_list:
        allin=word_list.read().strip()
    random_choice=random.sample(allin,5)
    return ''.join(random_choice)
WORLD_TO_SHOW=''
window=tk.Tk()
window.geometry('500x500')
window.resizable(False,False)
window.title('Lab3')
try:
    bg_image=tk.PhotoImage(file='img.png')
    bg_label=tk.Label(window,image=bg_image)
    bg_label.image=bg_image
    bg_label.place(x=0,y=0,relwidth=1,relheight=1)
except Exception as e:
    tk.messagebox.showwarning('error',"not found picture")
label_1=tk.Label(window,text="Please enter a 3-digit number:",font=('Verdanan',10))
label_1.place(relx=0.05,rely=0.2)

label_2=tk.Entry(window,width=3,font=('Verdana',10))
label_2.place(relx=0.5,rely=0.2)

label_3=tk.Label(window,text="keys:",font=("Verdana",10),wraplength=1000)
label_3.place(relx=0.1,rely=0.5)
def destory():
    window.destroy()


def keys():
    global WORLD_TO_SHOW
    NUMBER=label_2.get()
    if len(NUMBER)!=3 or not NUMBER.isdigit():
        tk.messagebox.showwarning('error','Please input NUMBER')
        label_2.delete(0,tk.END)
        return
    WORLD_TO_SHOW+=NUMBER
    label_4.configure(text=WORLD_TO_SHOW)
    keys_1=random_pick1()



    key_2=keys_1[:4]
    a=int(NUMBER[0])
    KEY_2=''
    for every in key_2:
        idx=allin.index(every)
        new_idx=(idx+a)%len(allin)
        KEY_2+=allin[new_idx]


    key_3=KEY_2[:3]
    KEY_3=''
    b=int(NUMBER[1])
    for ch in key_3:
        idx=allin.index(ch)
        new_idx_2=(idx-b)%len(allin)
        KEY_3+=allin[new_idx_2]

    key_4 = KEY_3[:2]
    KEY_4 = ''
    c = int(NUMBER[2])
    for ch in key_4:
        idx = allin.index(ch)
        new_idx_3 = (idx + c) % len(allin)
        KEY_4 += allin[new_idx_3]
    label_3.configure(text=f'keys: {keys_1}-{KEY_2}-{KEY_3}-{KEY_4}')




label_4=tk.Label(window,font=('Verdana',10))
label_4.place(relx=0.6,rely=0.6)
label_5=tk.Label(window,text="the number you entered",font=('Verdana',10))
label_5.place(relx=0.1,rely=0.6)
bt_1=tk.Button(window,text='Cancel',font=('Verdana',10),command=destory)
bt_1.place(relx=0.4,rely=0.7)

bt_2=tk.Button(window,text='OK',font=('Verdana',10),command=keys)
bt_2.place(relx=0.6,rely=0.7)
window.mainloop()




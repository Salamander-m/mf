from tkinter import *
from tkinter import messagebox
from random import *
from turtle import left
first = 0
second = 0
third = 0
def roll_message():
    first = randint(0,9)
    second = randint(0,9)
    third = randint(0,9)
    label_1 = Label(text=first)
    label_2 = Label(text=second)
    label_3 = Label(text=third)
    label_1.grid(row=0,column=0,columnspan=3)
    label_2.grid(row=0,column=10,columnspan=3)
    label_3.grid(row=0,column=20,columnspan=3)
    if first == 7 or second == 7 or third == 7:
        label_4 = Label(text='Счастливая сёмерка!')
        label_4.grid(row=0,column=40,columnspan=3)
    else:
        label_4 = Label(text='Не повезло, бывает(')
        label_4.grid(row=0,column=40,columnspan=3)
def exit_():
    exit()

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")


roll_button = Button(text="Крутить", command=roll_message)
roll_button.place(relx=.1, rely=.3, anchor="c")
exit_button = Button(text="Выход",command=exit_)
exit_button.place(relx=.10,rely=.5,anchor="c")

root.mainloop()
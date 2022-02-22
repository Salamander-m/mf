from tkinter import *
from tkinter import messagebox
 
def show_message():
    messagebox.showinfo("GUI Python", first.get() + second.get())
def edit_click():
    messagebox.showinfo("GUI Python", "Нажата опция Edit")
def file_click():
    messagebox.showinfo("GUI Python","Нажата опция File")
def view_click():
    messagebox.showinfo("GUI Python",'xD')
 
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")
 
main_menu = Menu()

file = Menu(main_menu,tearoff=0)
file.add_command(label="Открыть...")
file.add_command(label="Новый")
file.add_command(label="Сохранить...")
file.add_command(label="Выход")

main_menu.add_cascade(label="File",
                     menu=file)
 
main_menu.add_cascade(label="Edit", command=edit_click)
main_menu.add_cascade(label="View", command=view_click)

root.config(menu=main_menu)
# создание полей
first_label = Label(text="Введите первое число:")
second_label = Label(text="Введите второе число:") 

first_label.grid(row=0, column=0, sticky="w")
second_label.grid(row=1, column=0, sticky="w")
# созданаие данных для ввода
first = DoubleVar()
second = DoubleVar()

first_entry = Entry(textvariable=first)
second_entry = Entry(textvariable=second)

first_entry.grid(row=0,column=1, padx=5, pady=5)
second_entry.grid(row=1,column=1, padx=5, pady=5)

message_button = Button(text="Высчитать сумму", command=show_message)
message_button.place(relx=.5, rely=.5, anchor="c")


root.mainloop()
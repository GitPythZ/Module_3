import tkinter as tk


def get_values():
   num1 = int(number1_entry.get())
   num2 = int(number2_entry.get())
   return num1, num2


def insert_values(value):
   answer_entry.delete(0, "end")
   answer_entry.insert(0, value)


def add():
   num1, num2 = get_values()
   res = num1 + num2
   insert_values(res)

def sub():
   num1, num2 = get_values()
   res = num1 - num2
   insert_values(res)


def mult():
   num1, num2 = get_values()
   res = num1 * num2
   insert_values(res)


def div():
   num1, num2 = get_values()
   res = num1 / num2
   insert_values(res)


window = tk.Tk()
window.title("Калькулятор")
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text="+", width=3, height=2, command=add) #command=name_func - связывает кнопку с функцией
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text="-", width=3, height=2, command=sub)
button_sub.place(x=130, y=200)
button_mul = tk.Button(window, text="*", width=3, height=2, command=mult)
button_mul.place(x=160, y=200)
button_div = tk.Button(window, text="/", width=3, height=2, command=div)
button_div.place(x=190, y=200)
number1_entry = tk.Entry()
number1_entry.place(x=100, y=100)
number2_entry = tk.Entry()
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry()
answer_entry.place(x=100, y=275)
number1 = tk.Label(window, text="Введите первое число")
number1.place(x=100, y=75)
number2 = tk.Label(window, text="Введите второе число")
number2.place(x=100, y=125)
answer = tk.Label(window, text="Ответ")
answer.place(x=100, y=250)
window.mainloop()
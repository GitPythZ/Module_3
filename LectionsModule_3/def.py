# def say_hello(): # обычная функция
#     print('Hello')
# say_hello()

# функции бывают: обычными, анонимными, принимающими и вовзращающие
# ПРИНИМАЮЩАЯ ФУНКЦИЯ
# def say_hello(name): # обычная функция
#     print('Hello', name)
# say_hello('Tolya')
# ВОЗВРАЩАЮЩАЯ ФУНКЦИЯ
# import random
# def lottery():
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win = random.choice(tickets)
#     return win
# win = lottery()
# print(win)

# ПРИНИМАЮЩАЯ_ВОВЗРАЩАЮЩАЯ ФУНКИЦЯ
# def lottery(mon, thue):
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(tickets)
#     tickets.remove(win1)
#     win2 = random.choice(tickets)
#     tickets.remove(win2)
#     print(mon, thue)
#     return win1, win2
# win1, win2 = lottery("mon", "thue")
# print(win1, win2)
# Если я не знаю, сколько параметров будет вноситься, то я могу использовать "*args'именованных параметров
# и "**kwargs" для именованных параметров
import random
def lottery(*args):
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    tickets.remove(win2)
    print(*args)
    return win1, win2
win1, win2 = lottery(1,2,3,4,5,6,7,8)
print(win1, win2)
# В принимающие функции можно задать параметр по умолчанию
def test(a=2, b=True):
    print(a, b)
test(*[1,2])
# Если параметры даны по умолчанию, то для их вывода не нужно к ним обращаться, пишу test()
# test (False, "OK") - я могу переназначить параметры по умолчанию при обращении к функции
# Если поставлю "*" перед списком, то каждый элемент списка заменит соответсввенно переменные
# Если без "*", то заменит первый параметр


def foo():
    return total + 1


total = 0
print(foo())


email_ = "abc@mail.ru"
if not email_.endswith(".ru"):
    print(email_)
else:
    print("Недопустимый символ в строке!")
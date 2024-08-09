def test_func(*params): # * перед параметром создает кортеж
    print(params)


test_func(1, 2, 3, 4, 5)

def test_func_1(*params):
    print("Type", type(params))
    print("Argument", params)


test_func_1(1, 2, 3, 4, 5)

def summator(*values):
    s = 0
    for i in values:
        s += i
    return s


print(summator(1, 2, 3, 4))

def summator(txt, *values, type="sum"):
    s = 0
    for i in values:
        s += i
    return f"{txt}{s} {type}"


print(summator("Сумма чисел равна: ", 1, 2, 3, 4))


def info(**values): # получился словарь
    print("Type", type(values))
    print("Argument", values)
    for keys, values in values.items():
        print(keys, values)


info(name="Tolya", course="Python")


def info(value, *types, name_student="Anatoliy", **values): # позиционный параметр, произвольное число позиционных,
    # именованный, произольное число именованных. ** - получился словарь
    print("Type", type(values))
    print("Argument", values)
    for keys, values in values.items():
        print(keys, values)
    print(types)
    print(value)


info("Пример функции с параметрами всех типов", 2, 3, 4, name_student="Tolya", Name = "Volodya", course="Python")

def my_sum(degree, *args, txt="Сумма чисел: "):
    s = 0
    for i in range(len(args)):
        s += args[i]**degree
    print(txt + ":", s)


my_sum(1, 1, 2, 3, 4, 5)
my_sum(2, 1, 2, 3, 4, 5**0.5, 5, txt="Сумма квадратов чисел")
my_sum(3, 1, 2, 3, 4, 5, txt="Сумма кубов чисел")

# Python3 program to count the number of times
# an object appears in a list using count() method

lst = ['Cat', 'Bat', 'Sat', 'Cat', 'Mat', 'Cat', 'Sat']

# To get the number of occurrences
# of each item in a list
print ([ [l, lst.count(l)] for l in set(lst)])

# To get the number of occurrences
# of each item in a dictionary
print (dict( (l, lst.count(l) ) for l in set(lst)))
#Допустим, нужно сравнить "BUSSE" и "Buße", или даже "BUSSE" и "BUẞE" — это всё считается одинаковыми словами в немецком языке.
# Рекомендуемый способ — использовать метод casefold, который преобразует строку в форму, пригодную для регистронезависимого сравнения.
# import unicodedata
#
# [unicodedata.name(char) for char in 'Й']
# ['CYRILLIC CAPITAL LETTER SHORT I']
#
# >>> [unicodedata.name(char) for char in 'Й']
# ['CYRILLIC CAPITAL LETTER I', 'COMBINING BREVE']
# import unicodedata
#
# def normalize_caseless(text):
#     return unicodedata.normalize("NFKD", text.casefold())
#
# def caseless_equal(left, right):
#     return normalize_caseless(left) == normalize_caseless(right)
#
#
# >>> caseless_equal('BUSSE', 'Buße')
# True
#
# >>> caseless_equal('Й', 'Й')
# True

# Как уже писали выше, можно добавить .casefold к переменной:
import random
dic = {"Hello": "Здравствуй", "Bye": "Пока", "Lesson": "Урок"}
arr1 = int(random.random() * 3)
key2 = list(dic.keys())
key3 = list(dic.values())
while True:
    arr1 = int(random.random() * 3)
    print("Введите перевод :", key2[arr1])
    z = input()
    x = key3[arr1]
    if z.casefold() == x.casefold():
        print("Перевод верный!")
        continue
    if z.casefold() == str("show"):
        print(dic)
        continue
    if z.casefold() == str("quit"):
        exit()
    else:
        print("Вы ввели неверный перевод!")
        continue
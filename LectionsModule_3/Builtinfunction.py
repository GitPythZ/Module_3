# int() --> int(input())
# float()
# bool()
# str()
# set()
# list()
# tuple()
# dict()
print(bool(""))
print(bool(None))
print(bool(0))
print(bool(1))
print(bool("a"))
# Неявные преобразования
types = None
if types:
    print("Неявное преобразование") # пока тайп "False" - выводиться значение не будет

types = 1
if types:
    print("Неявное преобразование")
a = tuple("abcde")
print(a)
b = list("abcde")
print(b)

salary = [1500, 2300.78, 1800, 3000.46, 5000, 1234.85]
print(len(salary))
print(sum(salary))
summa = 0
total = 0
for i in salary:
    summa += i
    total += 1
print(summa/total)
print(round(sum(salary)/len(salary), 2), ": Средняя зарплата в компании")
names = ["Mem", "gag", "lol", "fafaf", "ASDfaf", "qwe"]
zipped = dict(zip(names, salary))
print(zipped["Mem"], "k;mgdmkd")
# Часть вторая
a = [False, False, True] # есмли хотя бы один элемент истина - то возвращает истину
print(any(a))
a = [False, False, 0]
print(any(a))
a = ""
print(any(a))
b = [0, 0, 1]
print(all(b)) # если все элементы исмтина - вернет истину.
# Методы интроспекции
x = [1, 2, 3, 4, 0]
print(dir(x))
print(isinstance(a, str))
print(isinstance(x, list))
print(isinstance(x, int))
print(isinstance(x[0], int))
# или
print(type(a) == str)
y = [1, 1, 1, 1]
z = [1, 1, 1, 1]
u = y
print(id(y))
print(id(z))
print(id(u))
print(y == z) # TRUE
print(y is z) # False
print(y is u) # True

print(help(y))

def helper():
    """
    Это функция помощник
    """

    pass


print(help(helper))

print(helper.__doc__)

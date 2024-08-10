# Рекурсия
def get_multiplied_digits(number):
    """Напиши функцию, которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа."""
    str_number = str(number) # Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


print(get_multiplied_digits(40203))
print(get_multiplied_digits(4))
print(get_multiplied_digits(55555))
print(get_multiplied_digits(30204))

# Примечания:
# При преобразовании строки(str) в число(int) первые нули убираются. int('00123') -> 123.
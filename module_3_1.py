# Пространство имен.

calls = 0
def count_calls():
    """Функция подсчета вызовов нижележащих функций."""
    global calls
    calls += 1
    """Создаю функцию с параметром "строка"."""
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
    """Создаю вторую функцию с двумя параметрами."""
def is_contains(string, list_to_search):
    count_calls()
    if string in list_to_search:
        return True
    else:
        return False
print(string_info("Учеба_на_Питоне"))
print(string_info("Capybara"))
print(is_contains("Moscow", ["New York", "Moscow", "Odessa", "London"]))
print(is_contains("Moscow", ["Pekin", "Rome", "London", "Paris"]))
print(calls)

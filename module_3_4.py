# "Произвольное число параметров"
# Задача "Однокоренные":

def single_root_word(*other_words, root_word="Python"): #Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
    same_words = [] #Создайте внутри функции пустой список same_words, который пополнится нужными словами.
    for words in other_words:
        if words.lower() in root_word.lower():
            same_words.append(words)
    return print(same_words)


single_root_word("JavaScript", "Typescript", "C++", "Python", "pythOn", "PYTHON")
single_root_word("JavaScript", "java", "jaVA", "Typescript", "C++", "Python", root_word="JavaScript")
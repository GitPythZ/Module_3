# ЗАДАЧА - "РАССЫЛКА ПИСЕМ."
# 1) Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель
# и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
# Внутри функции реализовать следующую логику:
# Проверка на корректность e-mail отправителя и получателя.
# Проверка на отправку самому себе.
# Проверка на отправителя по умолчанию.
def send_email(message, recipient, *, sender="uversity.help@gmail.com"): # "sender" помечен как именованный параметр.
    """Создал функцию с двумя обычными аргументами и одним именованным"""
    # Проверка наличия ключевых символов перед отправкой письма.
    if not recipient.endswith((".ru", ".com", ".net")) and not sender.endswith((".ru", ".com", ".net")) \
            and "@" not in recipient and "@" not in sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif sender == recipient:
        print(f"Нельзя отправить письмо самому себе!")
    elif sender == "uversity.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    elif sender != "uversity.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email("Это сообщение для проверки связи",
           "vasyok1337gmail.com") # Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
send_email("Вы видите это сообщение как лучший студент курса!",
           "urban.fan@mail.ru'", sender="urban.info@gmail.com") # НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
send_email("Пожалуйста, исправьте задание",
           "urban.student@mail.ru", sender="urban.teacher@mail.uk'") # Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
send_email("Напоминаю самому себе о вебинаре",
           "urban.teacher@mail.ru", sender="urban.teacher@mail.ru") # Нельзя отправить письмо самому себе!
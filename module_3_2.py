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
    if sender == "uversity.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    if sender == recipient:
        print(f"Нельзя отправить письмо самому себе!")
        return
    if recipient.endswith((".ru", ".com", ".net")) and sender.endswith((".ru", ".com", ".net")) \
            and "@" in recipient and "@" in sender:
        return
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")


send_email("Доброго времени суток, поступил в ваше распоряжение, письмо для проверки связи",
           "nanatoliy26@gmail.com")
send_email("Доброго времени суток, поступил в ваше распоряжение, письмо для проверки связи",
           "nanatoliy26@gmail.com", sender="urban.info@gmail.com")
send_email("Доброго времени суток, поступил в ваше распоряжение, письмо для проверки связи",
           "urban.student@mail.ru", sender="urban.teacher@mail.uk'")
send_email("Доброго времени суток, поступил в ваше распоряжение, письмо для проверки связи",
           "uversity.help@gmail.com")
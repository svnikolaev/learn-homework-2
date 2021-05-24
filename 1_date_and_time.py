"""
Домашнее задание №2

Дата и время

[x] 1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
[x] 2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = datetime.now()
    yesterday = today - timedelta(days = 1)
    once_upon_a_time = today - timedelta(days = 30)
    print('Сегодня: ' + today.strftime('%Y-%m-%d'))
    print('Вчера: ' + yesterday.strftime('%Y-%m-%d'))
    print('30 дней назад: ' + once_upon_a_time.strftime('%Y-%m-%d'))

def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))

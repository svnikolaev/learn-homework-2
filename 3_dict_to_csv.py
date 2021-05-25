import csv
"""

Домашнее задание №2

Работа csv

[x] 1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
[x] 2. Запишите содержимое списка словарей в файл в формате csv

"""

LIST_OF_DICTS = [
    {'name': 'Robert', 'age': 12, 'job': 'student'},
    {'name': 'Martin', 'age': 23, 'job': 'intern'},
    {'name': 'Katey', 'age': 31, 'job': 'programmer'},
    {'name': 'Darleen', 'age': 40, 'job': 'pilot'},
]

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        fields = list(LIST_OF_DICTS[0].keys())
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        # writer.writerows(LIST_OF_DICTS)
        for row in LIST_OF_DICTS:
            writer.writerow(row)
    # print(list(LIST_OF_DICTS[0].keys()))

if __name__ == "__main__":
    main()

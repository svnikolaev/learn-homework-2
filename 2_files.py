"""
Домашнее задание №2

Работа с файлами


[x] 1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
[x] 2. Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
[x] 3. Подсчитайте количество слов в тексте
[x] 4. Замените точки в тексте на восклицательные знаки
[x] 5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf-8') as referat:
        text = referat.read()
    
    text_length = len(text)
    print("Длинна строки: " + str(text_length))

    words_count = len(text.split())
    print("Количество слов: " + str(words_count) )

    text_with_exclamations = text.replace(".", '!')
    with open('referat2.txt', 'w', encoding='utf-8') as referat:
        referat.write(text_with_exclamations)

if __name__ == "__main__":
    main()

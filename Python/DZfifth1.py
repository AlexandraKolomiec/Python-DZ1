""" Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла
"""

def file_path(fp: str) -> tuple():
    one = fp.rsplit('\\', 1)[0]
    two = one.split('.')
    three = fp.rsplit('\\', 1)[1]
    four = three.split('.')
    return tuple(two + four)
print(file_path('C:\\Users\\alexa\\OneDrive\\Документы\\ДЗ 1.sql'))


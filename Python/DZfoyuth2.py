""" Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление
"""

def two_num (** kwargs) -> dict[str, int]:
    result = {}
    for key, value in kwargs.items():
        result[value] = key
    return result
print(two_num(n = 25, p = 28, l = 11))


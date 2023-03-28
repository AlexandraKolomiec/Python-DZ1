import time
from typing import Callable
from functools import wraps
from functools import cache

"""Замыкания: Функция add_one_str принимает на вход один параметр в качестве начала
строки и возвращает локальную функцию add_two_str. (без круглых скобок. Функцию передаём)
● Функция add_two_str принимает вторую часть строки, соединяет её с первой и возвращает ответ.
● При вызове функций значения указывются в отдельных круглых скобках.
Первое попадает в параметр a. Далее часть строки: add_one_str('Hello')
возвращает функцию add_two_str и уже она вызывается и принимает аргумент во вторых скобках
"""
# def add_one_str(a: str) -> Callable[[str], str]:
#     def add_two_str(b: str) -> str:
#         return a + ' ' + b
#     return add_two_str
# print(add_one_str('Hello')('world!'))#Hello world!

"""Замыкаем функцию с параметрами"""
# def add_one_str(a: str) -> Callable[[str], str]:
#     def add_two_str(b: str) -> str:
#         return a + ' ' + b
#     return add_two_str
# hello = add_one_str('Hello')#переменные содержат результат работы ф-ции add_one_str с разными аргументами.
# bye = add_one_str('Good bye')#можем вызывать новые функции и получать объединённые строки передавая только окончание
# print(hello('world!'))
# print(hello('friend!'))
# print(bye('wonderful world!'))
# print(f'{type(add_one_str) = }, {add_one_str.__name__ = },{id(add_one_str) = }')
# print(f'{type(hello) = }, {hello.__name__ = }, {id(hello) = }')
# print(f'{type(bye) = }, {bye.__name__ = }, {id(bye) = }')

"""Во внешнюю функцию добавлен список names. При каждом вызове внутренней
функции в список добавляется новое значение из параметра b и возвращается
полное содержимое списка в виде строки. У каждой из двух функций hello и bye
оказывается свой список names. Они не связаны между собой, но каждый хранит
список имён до конца работы программы.
"""

# def add_one_str(a: str) -> Callable[[str], str]:
#     # names = []#list -изменяемый тип данных
#     text = ''#text
#     def add_two_str(b: str) -> str:
#         nonlocal text#добаляем для неизменяемых типов -text
#         #names.append(b)
#         #return a + ', ' + ', '.join(text)
#         text += ', ' + b#text
#         return a + text#text
#     return add_two_str
# hello = add_one_str('Hello')
# bye = add_one_str('Good bye')
# print(hello('Alex'))
# print(hello('Karina'))
# print(bye('Alina'))
# print(hello('John'))
# print(bye('Neo'))

#42 в степени от 0 до 7 {0: 1, 1: 42, 2: 1764, 3: 74088, 4: 3111696, 5: 130691232, 6: 5489031744}
#73 в степени от 0 до 7 {0: 1, 1: 73, 2: 5329, 3: 389017, 4: 28398241, 5: 2073071593, 6: 151334226289}
#42 в степени от 0 до 7 {0: 1, 1: 42, 2: 1764, 3: 74088, 4: 3111696, 5: 130691232, 6: 5489031744}

# def main(x: int) -> Callable[[int], dict[int, int]]:
#     d = {}
#     def loc(y: int) -> dict[int, int]:
#         for i in range(y):
#             d[i] = x ** i
#         return d
#     return loc
# small = main(42)
# big = main(73)
# print(small(7))
# print(big(7))
# print(small(3))

"""Декораторы @main: Функция main принимает на вход другую функцию. Внутри функции
определена функция wrapper, которая возвращается функцией main.
● Функция wrapper принимает пару параметров *args и **kwargs(позволяет принять любое число позиционных
аргументов и сохранить их в кортеже args, а также любое число ключевых
аргументов с сохранением в словаре kwargs.)
Обязательной строкой внутри wrapper является result = func(*args, **kwargs).
Переданная в качестве аргумента функция func вызывается со всеми
аргументами, которые были переданы. Дополнительно выводим информацию
о времени запуска, результатах и времени завершения работы функции. Не
забываем вернуть результат работы func из wrapper.● Функция factorial вычисляет факториал для заданного числа
ответ
Запуск функции factorial в 1679421078.1715999
Результат функции factorial:значение факториал от 1000
Завершение функции factorial в 1679421185.3929317
factorial(1000) =значение факториал от 1000
"""


# def main(func: Callable):
#     def wrapper(*args, **kwargs):
#         print(f'Запуск функции {func.__name__} в {time.time()}')
#         result = func(*args, **kwargs)
#         print(f'Результат функции {func.__name__}: {result}')
#         print(f'Завершение функции {func.__name__} в {time.time()}')
#         return result
#     return wrapper
# @main
# def factorial(n: int) -> int:
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
# print(f'{factorial(1000) = }')

""" Множественное декорирование. Прежде чем выполнить код основной функции запускается код верхнего
декоратора С, далее B, в конце нижний A и только потом код функции main. После
того как декорированная функция завершила работу и вернула результат
декораторы завершают работу в обратном старту порядке, снизу вверх.
Возвращаем декоратор A
Возвращаем декоратор B
Возвращаем декоратор C
Старт декоратора C
Запускаю wrapper_b
Старт декоратора B
Запускаю wrapper_a
Старт декоратора A
Запускаю main
Старт основной функции
Завершение декоратора A
Завершение декоратора B
Завершение декоратора C"""

# def deco_a(func: Callable):
#     def wrapper_a(*args, **kwargs):
#         print('Старт декоратора A')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора A')
#         return res
#     print('Возвращаем декоратор A')
#     return wrapper_a

# def deco_b(func: Callable):
#     def wrapper_b(*args, **kwargs):
#         print('Старт декоратора B')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора B')
#         return res
#     print('Возвращаем декоратор B')
#     return wrapper_b

# def deco_c(func: Callable):
#     def wrapper_c(*args, **kwargs):
#         print('Старт декоратора C')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора C')
#         return res
#     print('Возвращаем декоратор C')
#     return wrapper_c

# @deco_c
# @deco_b
# @deco_a
# def main():
#     print('Старт основной функции')
# main()

"""Декоратор с параметрами"""

# def count(num: int = 1):#Внешняя функция count принимает на вход целое число num. Данный параметр будет использован для цикла for
#     def deco(func: Callable):#Функция deco принимает декларируемую функцию
          #@wraps(func)#добавляется к самой глубоко вложенной функции. В качестве аргумента wraps должен получить параметр декларируемой функции.
#         def wrapper(*args, **kwargs):#Внутренняя функция wrapper создаёт список time_for_count для хранения результатов замеров быстродействия
#             time_for_count = []
#             result = None
#             for _ in range(num):
#                 start = time.perf_counter()#замеряем текущее время. рекомендуется использовать модуль timeit
#                 result = func(*args, **kwargs)#выполняем функцию
#                 stop = time.perf_counter()#сохраняем результат в переменную
#                 time_for_count.append(stop - start)#Замеряем время после окончания работы функции и сохраняем разницу в список
#             print(f'Результаты замеров {time_for_count}')#сообщаем результаты из списка time_for_coun
#             return result#возвращаем результат работы декларируемой функции
#         return wrapper
#     return deco

# @count(10)#Запускаем цикл for столько раз, сколько мы передали в декоратор=10
# def factorial(n: int) -> int:#делаем 10 замеров и смотрим время на вычисления
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
# print(f'{factorial(1000) = }')
# print(f'{factorial(1000) = }')
##print(f'{factorial.__name__ = }')#@wraps
##help(factorial)#@wraps

"""Только первые вызовы запускают функцию. Повторный вызов с уже передававшимся аргументом обрабатывается декоратором cache
factorial(20) = 2432902008176640000
factorial(10) = 3628800
factorial(20) = 2432902008176640000"""
@cache
def factorial(n: int) -> int:

    print(f'Вычисляю факториал для числа {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

print(f'{factorial(10) = }')
print(f'{factorial(15) = }')
print(f'{factorial(10) = }')
print(f'{factorial(20) = }')
print(f'{factorial(10) = }')
print(f'{factorial(20) = }')
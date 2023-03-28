""" Создайте функцию-замыкание, которая запрашивает два целых числа:
от 1 до 100 для загадывания,
от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль 
просит угадать загаданное число за указанное число попыток.
"""

from typing import Callable

# def deco(a: int, count: int) -> Callable [[], None]:
    
#     def ugadai() -> None:

#         for i in range(count):
#             num = int(input('Введите число 1 - 100: '))
#             if num > a:
#                 print('Число больше')
#             elif num < a:
#                 print('Число меньше')
#             else:
#                 print('Вы угадали ')
#                 break
#     return ugadai

# game = deco(20, 5)
# game()

""" Дорабатываем задачу 1. 
Превратите внешнюю функцию в декоратор. 
Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10]. 
Если не входят, вызывать функцию со случайными числами из диапазонов.
"""
# import random

# def deco(func):
#     def wrapper(a: int, count: int, ):#*args, **kwargs
#         if a < 1 or a > 100:
#             a = random.randint(1,101)
            
#         if count < 1 or count > 10:
#             count = random.randint(1,11)
#         result = func(a, count)
#         return result
#     return wrapper

# @deco
# def ugadai(a: int, count: int) -> None:

#     for i in range(count):
#         num = int(input('Введите число 1 - 100: '))
#         if num > a:
#             print('Число больше')
#         elif num < a:
#             print('Число меньше')
#         else:
#             print('Вы угадали ')
#             break

# ugadai(108, 17)   

""" Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
При повторном вызове файл должен расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции.
"""
import json
from pathlib import Path

# def deco_file(func):
#     file = Path(f'{func.__name__}.json')#Имя файла должно совпадать с именем декорируемой функции
#     if file.is_file():
#         with open(file, 'r', encoding='utf-8') as f:
#             data = json.load(f)
#     else:
#         data =[]
#     def wrapper(*args, **kwargs):
#         new_data = {'args':args, **kwargs}#ключевой параметр сохраните как отдельный ключ json словаря
#         result = func(*args, **kwargs)#принимать как позиционные, так и ключевые аргументы
#         data.append(new_data)
#         with open(file, 'w', encoding='utf-8') as f:#'w' для json вместо 'a'
#             json.dump(data, f)#При повторном вызове файл должен расширяться, а не перезаписываться
#         return result
#     return wrapper


# @deco_file
# def call(*args, **kwargs):
#     pass


# call(31,15,178, x = 18, z = 'a')

"""Создайте декоратор с параметром. 
Параметр - целое число, количество запусков декорируемой функции."""
import time

def count(num: int = 1):#Внешняя функция count принимает на вход целое число num. Данный параметр будет использован для цикла for
    def deco(func: Callable):#Функция deco принимает декларируемую функцию
        # @wraps(func)#добавляется к самой глубоко вложенной функции. В качестве аргумента wraps должен получить параметр декларируемой функции.
        def wrapper(*args, **kwargs):#Внутренняя функция wrapper создаёт список time_for_count для хранения результатов замеров быстродействия
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()#замеряем текущее время. рекомендуется использовать модуль timeit
                result = func(*args, **kwargs)#выполняем функцию
                stop = time.perf_counter()#сохраняем результат в переменную
                time_for_count.append(stop - start)#Замеряем время после окончания работы функции и сохраняем разницу в список
            print(f'Результаты замеров {time_for_count}')#сообщаем результаты из списка time_for_coun
            return result#возвращаем результат работы декларируемой функции
        return wrapper
    return deco

@count(10)#Запускаем цикл for столько раз, сколько мы передали в декоратор=10
def factorial(n: int) -> int:#делаем 10 замеров и смотрим время на вычисления
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
print(f'{factorial(10) = }')
print(f'{factorial(10) = }')
#print(f'{factorial.__name__ = }')#@wraps
#help(factorial)#@wraps
    
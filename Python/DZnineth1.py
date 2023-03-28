""" 1.Написать функции:
-Нахождение корней квадратного уравнения
-Генерации csv файла с 3 случайными числами в каждой строке 100-1000 строк
-Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждойй тройкой чисел из csv файла
-Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл
2. Соберите пакет из файлов
"""
import random
import csv
from typing import Callable
import json
__all__ = ['deco_csv', 'deco_json', 'csv_file', 'square']

#декоратор функции нахождения корней квадратного уравнения с каждойй тройкой чисел из csv файла
def deco_csv(func: Callable):
    def wrapper():
        with open('3_numbers.csv', 'r', newline='', encoding='utf-8') as file:
            a = csv.reader(file)
            result = []
            for rows in a:
                [a, b, c] = int(rows[0]), int(rows[1]), int(rows[2])
                result.append(func(a, b, c))
            return result

    return wrapper

#декоратор функции сохраняющий переданные параметры и результаты работы функции в json файл
def deco_json(func: Callable):
    def wrapper():
        result = func()
        with open('3_numbers.json', 'w') as f:
            json.dump(result, f, indent=1)

    return wrapper

#Нахождение корней квадратного уравнения
@deco_json 
@deco_csv 
def square(k: int, m: int, n: int) -> int:
    disc = abs(m * 2 - 4 * k * n)
    result = round((- m + (disc * 0.5)) / (2 * k), 4)
    result2 = round((- m - (disc ** 0.5)) / (2 * k), 4)
    d = [f'{result}, {result2}]']
    return d


square()

#Генерация csv файла с 3 случайными числами
def csv_file():
    sn = []
    for i in range(random.randint(100, 1000)):
        s = []
        sn.append(s)
        for _ in range(3):
            l: int = random.randint(1, 999)
            s.append(str(l))
    with open('3_numbers.csv', 'w', newline='', encoding='utf-8') as file:
        csv_write = csv.writer(file)
        for row in sn:
            csv_write.writerow(row)


csv_file()



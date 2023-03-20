""" Создайте файл, в котором вы импортируете встроенные в 
модуль функции под псевдонимами. (3-7 строк импорта).
"""
from sys import argv
import random as rnd
import csv as c #работа с электронными таблицами
import unittest as ut #автоматизация тестов
import fractions as fr #рациональные числа
import cmath as ch # комплексные числа

""" Создайте модуль с функцией внутри. 
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. 
Внутри генерируется случайное число в указанных границах и пользователь
 должен угадать его за заданное число попыток. Функция выводит подсказки “больше” и “меньше”. 
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""
# def guess(down:int, up:int, chanse:int) -> bool:
#     number = rnd.randint(down, up)

#     for i in range(chanse):
#         print(f"Enter number from {down} to {up} ")
#         num = int(input())
#         if num > number:
#             print(" Number is smaller ")
#         elif num < number:
#             print(" Number is bigger ")
#         else:
#             return True
#     return False      


# if __name__ == '__main__':

#     down = int(input('Enter first number: '))
#     up = int(input('Enter second number: '))
#     chanse = int(input('Enter third number: '))
#     print(guess(down, up, chanse))

""" Улучшаем задачу 2. 
Добавьте возможность запуска функции “угадайки” из модуля в
 командной строке терминала. Строка должна принимать от 1 до
 3 аргументов: параметры вызова функции. Для преобразования
 строковых аргументов командной строки в числовые параметры 
 используйте генераторное выражение.
 """
# def guess(down:int = 0, up:int = 10, chanse:int = 5 ) -> bool:
#     number = rnd.randint(down, up)

#     for i in range(chanse):
#         print(f"Enter number from {down} to {up} ")
#         num = int(input())
#         if num > number:
#             print(" Number is smaller ")
#         elif num < number:
#             print(" Number is bigger ")
#         else:
#             return True
#     return False      


# if __name__ == '__main__':
#     tmp_path, * params = argv

    
#     print(guess(*(int (n) for n in params )))

# # в терминале папки вводим в командную строку python py6.py 2 10 3

"""Создайте модуль с функцией внутри. 
Функция получает на вход загадку, список с возможными
вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана
загадка или ноль, если попытки исчерпаны.
 """
# def mystery(m:str, answer:list, chanse: int) -> int:
    
#     print(m)
#     for i in range(chanse):
#         ans = input(' Введите ответ ')
#         if  ans in answer:
#             return i + 1
#     return 0
      


# if __name__ == '__main__':

#     m = 'Зимой и летом одним цветом! '
#     an = ['Елка', 'Ель', 'Елочка']
#     ch = 5
#     print(mystery(m, an, ch))
    
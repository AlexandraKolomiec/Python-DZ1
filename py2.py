#1Создайте несколько переменных разных типов. Проверьте к какому типу относятся созданные переменные.
# b = 7
# b = 7.35
# txt = 'message'
# c = {1, 2, 3}
# d = True

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(txt))

#2 Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты

# import sys

# data = ['text', 4, 4.65, True, 455, 'trrw']
# for i, num in enumerate(data, start=1):
#     print(i, num, id(num), sys.getsizeof(num), hash(num), end=" ")
#     if (isinstance(num, int)):
#         print("Это число")
#     elif(isinstance(num, str)):
#         print("Это строка")
#     else:
#         print()

#3 Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
#✔ Функции bin и oct используйте для проверки своего результата, а не для решения

number: int = int(input("Enter number "))
number1: int = number
DOUBLE = 2
OCT = 8

print(bin(number))
print(oct(number))

for i in DOUBLE, OCT:
    number = number1
    result: str = ""
    while number > 0:
        double_num: int = number % i
        result = str(double_num) + result 
        number = number // i
    print(result)

#4 Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять не менее 42 знаков после запятой.

# import math
# import decimal

# decimal.getcontext().prec=42
# diametr = decimal.Decimal(input("Enter diametr  "))
# pi = decimal.Decimal(math.pi)
# MAX_LIMIT = 1000

# if diametr > MAX_LIMIT:
#     print("Enter number less than 1000")
# else:
#     length = pi * diametr
#     square = pi * (diametr/2) ** 2
#     print(length, square)
 
#5 Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный

# a = int(input(" Enter first number "))
# b = int(input(" Enter second number "))
# c = int(input(" Enter third number "))

# disc = abs(b ** 2 - 4 * a * c)
# result = (- b + (disc ** 0.5)) / (2 * a)
# result2 = (- b - (disc ** 0.5)) / (2 * a)
# print(result, result2)




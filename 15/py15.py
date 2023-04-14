"""Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
📌 Например отлавливаем ошибку деления на ноль."""

import logging

# FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
# logging.basicConfig(level=logging.ERROR, filename='C:\\Users\\alexa\\OneDrive\\Рабочий стол\\Python\\15\\ZeroDivisionError.log', encoding='utf-8',
#                     format=FORMAT, style="{")
# logger = logging.getLogger(__name__)


# def func_div_two(a, b) -> float:
#     try:
#         res = a / b
#     except ZeroDivisionError as e:
#         logger.error(f'Ошибка деления числа {a} на число {b}')
#         return float('inf')
#     return res


# if __name__ == '__main__':
#     print(func_div_two(8, 0))

"""На семинаре про декораторы был создан логирующий декоратор.
 Он сохранял аргументы функции и результат её работы в файл. 
 Напишите аналогичный декоратор, но внутри используйте модуль logging.
 3.Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает. При повторном вызове 
 файл должен расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции.
"""

# FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
# logging.basicConfig(level=logging.INFO, filename='C:\\Users\\alexa\\OneDrive\\Рабочий стол\\Python\\15\\deco1.log', encoding='utf-8', style="{")
# logger = logging.getLogger(__name__)

# def deco_file(func):
#     data = []
#     def wrapper(*args, **kwargs):
        
#         new_data = {'args': args, **kwargs}
#         result = func(*args, **kwargs)
#         data.append(new_data)
#         # print(new_data)
#         logger.info(new_data)
#         return result
#     return wrapper

# @deco_file
# def call(*args, **kwargs):
#     pass

# call(12, 24, 56, ax = 12, b = 45)

"""Доработаем задачу 2.
Сохраняйте в лог файл раздельно: ○ уровень логирования, ○ дату события, ○ имя функции (не декоратора), ○ аргументы вызова, ○ результат."""

# FORMAT = '{levelname} - {asctime} : {msg}'
# logging.basicConfig(level=logging.INFO, filename='C:\\Users\\alexa\\OneDrive\\Рабочий стол\\Python\\15\\deco1.log', encoding='utf-8', format=FORMAT, style="{")
# logger = logging.getLogger(__name__)

# def deco_file(func):
#     data = []
#     def wrapper(*args, **kwargs):
        
#         new_data = {'args': args, **kwargs}
#         result = func(*args, **kwargs)
#         data.append(new_data)
#         # print(new_data)
#         logger.info(f' {func.__name__}{new_data}')
#         return result
#     return wrapper

# @deco_file
# def call(*args, **kwargs):
#     pass

# call(12, 24, 56, ax = 12, b = 45)

"""Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
📌 Преобразуйте его в дату в текущем году.
📌 Логируйте ошибки, если текст не соответсвует формату."""

from datetime import datetime
from calendar import monthrange

FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
logging.basicConfig(level=logging.ERROR, filename='C:\\Users\\alexa\\OneDrive\\Рабочий стол\\Python\\15\\data_text.log', encoding='utf-8',
                    format=FORMAT, style="{")
logger = logging.getLogger(__name__)

MONTH = ('янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя','дек')
DAY = ("пон", "вто", "сре", "чет", "пят", "суб","вос")


def data_text(text: str) -> datetime:
    try:
        count, day, month = text.split()
    except ValueError as e:
        logger.error(f'Ошибка введения даты')
        return None
    #срезы по дате и месяцу
    count = int(count[:-2])
    day = DAY.index(day[:3])
    month = MONTH.index(month[:3]) + 1
    # текущий год
    year = datetime.now().year
    #  возвращает двойной кортеж c первым рабочем днем месяца и количество дней в месяце для указанного года year и месяца month
    count_days = monthrange(year, month)[1]
    # print(count_days)
    count_week = 0
    for d in range(1, count_days+1):
        date = datetime(day= d, month= month, year= year)
        # Получить день недели как int
        if date.weekday() == day:
            # print(date)
            count_week += 1
            if count == count_week:
                return date

print(data_text('3-я среда мая'))

 
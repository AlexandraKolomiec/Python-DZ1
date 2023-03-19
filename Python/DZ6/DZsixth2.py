""" Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
 Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
Проверку года на високосность вынести в отдельную защищённую функцию.
"""

from datetime import date

__all__ = ['date_check', 'leap']

def date_check(d:int, m: int, y: int) -> bool:
    try:
        date(y, m, d)
        return True
    except:
        return False

def leap(y: int) -> bool:
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    else:
        return False  


if __name__ == '__main__':
    e = input('Enter date as DD.MM.YYYY: ')
    a, b, c = e.split('.')
    d = int(a)
    m = int(b)
    y = int(c)
    print(date_check(d, m, y), leap(y))
    

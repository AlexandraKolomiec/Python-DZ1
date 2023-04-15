""" Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число. Обрабатывайте не числовые данные как исключения"""

import logging


FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
# logging.basicConfig(level=logging.ERROR)#вывод в терминал
logging.basicConfig(level=logging.ERROR, filename='C:\\Users\\alexa\\OneDrive\\Рабочий стол\\Python\\Python\\DZ15\\get_numbers.log', encoding='utf-8',
                    format=FORMAT, style="{")
logger = logging.getLogger(__name__)


def get(text: str = None) -> int:
    while True:
        data = input(text)
        try:
            num = float(data)
            break
        except ValueError as e:
            logger.error(f'Введенное значение {data} не является целым или вещественным числом ')
            print(f'Ввод привёл к ошибке ValueError: {e}\n'
            f'Попробуйте снова')
    return num
if __name__ == '__main__':

    number = get('Введите число: ')
    print(number)
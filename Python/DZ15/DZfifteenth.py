"""Возьмите любые 1-3 задачи из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из
командной строки с передачей параметров."""

"""Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. 
Внутри генерируется случайное число в указанных границах и пользователь
 должен угадать его за заданное число попыток. Функция выводит подсказки “больше” и “меньше”. 
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""

import random as rnd
import logging

FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
logging.basicConfig(level=logging.INFO, filename='C:\\Users\\alexa\\OneDrive\\Рабочий стол\\Python\\Python\\DZ15\\guess.log', encoding='utf-8', style="{")
logger = logging.getLogger(__name__)

def guess(down:int, up:int, chance:int) -> bool:
    number = rnd.randint(down, up)
    logger.info(f'lower limit {down},  upper limit {up}, number of attempts {chance}')
    logger.info(f'hidden number is: {number}')

    for i in range(chance):
        print(f"Enter number from {down} to {up} ")
        num = int(input())
        if num > number:
            print(" Number is smaller ")
            logger.info(f'entered number: {num}')
        elif num < number:
            print(" Number is bigger ")
            logger.info(f'entered number: {num}')
        else:
            logger.info('number guessed!')
            return True
    logger.info('the chances are over')
    return False      


if __name__ == '__main__':

    down = int(input('Enter first number: '))
    up = int(input('Enter second number: '))
    chance = int(input('Enter third number: '))
    print(guess(down, up, chance))



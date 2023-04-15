import argparse
import logging

FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def get(text: str = None) -> int:
    while True:
        data = input(text)
        try:
            num = float(data)
            break
        except ValueError as e:
            logger.error(f'Введенное значение {text} не является целым или вещественным числом ')
            print(f'Ввод привёл к ошибке ValueError: {e}\n'
            f'Попробуйте снова')
    return num

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Запрос числовых данных')
    parser.add_argument('param', type=str,  help='Введите число: ')
    args = parser.parse_args()
    print(get(args.param))


"""PS C:\Users\alexa\OneDrive\Рабочий стол\Python\Python\DZ15> python DZfifteenth3.py 2
2
ERROR:__main__:Введенное значение 2 не является целым или вещественным числом
Ввод привёл к ошибке ValueError: could not convert string to float: ''
Попробуйте снова
22
2.0"""
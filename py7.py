"""Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции 
"""
import random as rnd

# def file_in(a: int, b: str) -> None :
    
#     with open('text_file.txt', 'w', encoding='utf-8') as f:
#         for i in range(a):
#             inumber = rnd.randint(-1000,1000)
#             fnumber = rnd.uniform(-1000,1000)
        
#             f.write(f'{str(inumber)} | {str(fnumber)} \n')
            
# file_in(5,'text_file.txt')

"""Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы,состоять из 4-7 букв, среди которых обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
 """
glas_str = "уеыаоэяию"
sogl_str = "йцкнгшщзхфвпрлджчсмтб"
def func(cnt_line:int, file_name:str):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(cnt_line):
            result_str = ""
            for i in range(rnd.randint(4,7)):
                result_str += glas_str[rnd.randint(0, len(glas_str)-1)] \
                        + sogl_str[rnd.randint(0, len(sogl_str)-1)]
            
            result_str = result_str.capitalize()

            print(result_str)
            f.write(f'{result_str}\n')

func(5, "data.txt")

""" Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
✔ если результат умножения отрицательный, сохраните имя записанное строчными  буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,сколько в более длинном файле.
✔ При достижении конца более короткого файла,возвращайтесь в его начало
"""
def open_files(a:str, b:str) ->None:
    with (
        open(a, 'r', encoding='utf-8') as f1,
        open(b, 'r', encoding='utf-8') as f2,
        open('new_file.txt', 'w', encoding='utf-8') as f3
        ): 
            lenf1 = sum(1 for i in f1)
            lenf2 = sum(1 for i in f2)
            print(lenf1, lenf2) # находим кол-во строк в файлах
            for i in range(max(lenf1, lenf2)):
                  text = f2.readline()
                  if text == '':
                        f2.seek(0)# переход в начало
                        text = f2.readline()
                  text = text[: -1]#убираем последний символ
                  num = f1.readline()
                  if num == '':
                        f1.seek(0)
                        num = f1.readline()
                  num = num.replace(' ', '')[:-1]#замена пробелов
                  num1, num2 = num.split('|')
                  
                  res_mult = int(num1) * float(num2)
                  if res_mult < 0:
                        f3.write(f'{text.lower()},{abs(res_mult)} \n')
                  else:
                        f3.write(f'{text.upper()},{round(res_mult)}\n')
                        
                  print(text, num1, num2, res_mult)
               

open_files('text_file.txt','data.txt')







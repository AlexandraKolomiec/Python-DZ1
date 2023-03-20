"""Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла
 новый с данными в формате JSON. Имена пишите с большой буквы. 
Каждую пару сохраняйте с новой строки.
 """

import json

# def convert(file_name: str)-> None:
#     dic = {}
#     with open(file_name, 'r', encoding='utf-8') as f:
#         for line in f:
#             li = line.split(',')
            
#             dic[li[0].capitalize()] = float(li[1])
#         #print(dic)
#     with open('file_json.json', 'w', encoding='utf-8') as f:
#         json.dump(dic, f, ensure_ascii=False, indent=2)# indent=2 перенос на новую строку
# convert('new_file.txt')

"""Напишите функцию, которая в бесконечном цикле запрашивает имя,
 личный идентификатор и уровень доступа (от 1 до 7). 
После каждого ввода добавляйте новую информацию в JSON файл. 
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени. 
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа. 
При перезапуске функции уже записанные в файл данные должны сохраняться. 
"""

def ident(name_file: str):
    dic ={}
    second = {}
    with open(name_file, 'r', encoding='utf-8') as f:#чтение файла
        data = json.load(f)#запись данных в файл
    dic = data#сохранение
    print(type(dic))
    print(dic)
    while True:
        name = input("введите имя ")
        if name == '':#выход из цикла
            break
        id = int(input("введите личный идентификатор "))
        lev = input('введите уровень доступа (от 1 до 7) ')#строковое значение- ключ!
        second = {id:name}#словарь в словаре с идент lev
        
        if dic.get(lev) is None:#проверка на уникальность ключа
            dic[lev] = second
        else:
            k = dic.get(lev) 
            k.update(second)      
    print(dic) 
    with open(name_file, 'w', encoding='utf-8') as f:
        
        json.dump(dic, f, ensure_ascii=False, indent=2)
    
   
ident('ident.json')        

  
 

    
        
    
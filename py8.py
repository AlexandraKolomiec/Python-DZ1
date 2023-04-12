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

def user_access(name_file: str):
    dict_lev = {}
    dict_user = {}
    with open(name_file, 'r', encoding='utf-8') as f:
        data_file = json.load(f)
        dict_lev = data_file
    while True:
        name = input('Enter name: ')
        if name == '':
            break
        id_user = int(input('Enter id: '))
        lev = input('Enter your level (1 - 7): ')
        dict_user[id_user] = name

        if dict_lev.get(lev) is None:
            dict_lev[lev] = dict_user
        else:
            key_lev = dict_lev.get(lev)
            key_lev.update(dict_user)

    print(dict_lev,dict_user)
    with open(name_file, 'w', encoding='utf-8') as f:
        json.dump(dict_lev, f, ensure_ascii=False, indent=2)




if __name__ == '__main__':
    user_access('indent.json')

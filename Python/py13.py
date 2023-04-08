""" Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число. Обрабатывайте не числовые данные как исключения"""

# def get(text: str = None) -> int:
#     while True:
#         data = input(text)
#         try:
#             num = float(data)
#             break
#         except ValueError as e:
#             print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
#             f'Попробуйте снова')
#     return num
# if __name__ == '__main__':

#     number = get('Введите число: ')
#     print(number)

"""Создайте функцию аналог get для словаря.
📌 Помимо самого словаря функция принимает ключ и
значение по умолчанию.
📌 При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
📌 Реализуйте работу через обработку исключений. """

# def get_dict(user_dict, key_dict, val_d=None):

#     try:
#         res = user_dict[key_dict]
#         return res
#     except KeyError as k:
#         return f'Нет такого ключа, дефолтное значение {val_d}'


# user = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
# if __name__ == '__main__':
#         print(get_dict(user, 5))

""" Создайте класс с базовым исключением и дочерние классы-
исключения:
○ ошибка уровня,
○ ошибка доступа"""

# class BaseException(Exception):
#     pass

# class LevelException(BaseException):
#     print('Level')

# class AccesException(BaseException):
#     print('Access')

"""Вспоминаем задачу из семинара 8 про сериализацию данных,где в бесконечном цикле запрашивали имя, личный идентификатор
 и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
📌 Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
📌 Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей """
# import json


# class User:
#     def __init__(self, name :str, id: int, level: int):
#         self.name = name
#         self.id = id
#         self.level = level
   
# def reed_json(file_name: str):
#     users = set()
#     with open(file_name, 'r', encoding='utf-8') as f:
#         data = json.load(f)
    
#     for level, value in data.items():
#         for id, name in value.items():
#             users.add(User(name = name,id= int(id),level= int(level)))
#     return users
      
# print(reed_json('ident.json'))

""" Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
📌 загрузка данных (функция из задания 4)
📌 вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из множества пользователей.
📌 добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа."""

import json
from user_exception import LevelException, AccesException

class User:
    def __init__(self, name :str, id: int, level: int):
        self.name = name
        self.id = id
        self.level = level
    #метод проверки на равенство пользователей
    def __eq__(self, other) -> bool:
        return self.id == other.id and self.name == other.name

class Project:
    def __init__(self) -> None:
        self.users = set()
        self.user = None

    def reed_json(self, file_name: str):
        
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for level, value in data.items():
            for id, name in value.items():
                self.users.add(User(name = name,id= int(id),level= int(level)))
        return self.users

    #print(reed_json('ident.json'))
    def enter(self, name: str, id: int):
        u1 = User(name= name, id= id, level= 0)
        print(u1)
        if u1 not in self.users:
            raise AccesException
        
        for item in self.users:
            if u1 == item:
                self.user = item
                return self.user

#     def add_user(self, name: str, id: int, level: int):

#         if level < self.user:
#             raise LevelException
        

# u2 = Project()
# u2.enter("Fil", 88 )

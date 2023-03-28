""" Создайте класс окружность. 
Класс должен принимать радиус окружности при создании 
экземпляра. У класса должно быть два метода, возвращающие 
длину окружности и её площадь
"""
# import math
# class Round:
#     def __init__(self, radius: float) -> None:
#         self.radius = radius
    
#     def length(self):
#         return 2 * math.pi * self.radius
    
#     def square(self):
#      return math.pi * self.radius ** 2
# round = Round(10)
# print(round.length(), round.square())

""" Создайте класс прямоугольник. 
Класс должен принимать длину и ширину при создании экземпляра. 
У класса должно быть два метода, возвращающие периметр и площадь. 
Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
"""
# class Rectangle:

#     def __init__(self, side_a: float, side_b=None):
#         self.side_a = side_a
#         if side_b is None:
#             self.side_b = side_a
#         else:
#             self.side_b = side_b

#     def square_rectangle(self):
#         return self.side_a * self.side_b

#     def len_rectangle(self):
#         return (self.side_a + self.side_b) * 2


# rect = Rectangle(5, 10)
# print(rect.len_rectangle(), rect.square_rectangle())

# class Rectangle:

#     def __init__(self, side_a: float, side_b=None):
#         self.side_a = side_a
#         if side_b is None:
#             self.side_b = side_a
#         else:
#             self.side_b = side_b

#     def square_rectangle(self):
#         return self.side_a * self.side_b

#     def len_rectangle(self):
#         return (self.side_a + self.side_b) * 2


# rect = Rectangle(5, 10)
# print(rect.len_rectangle(), rect.square_rectangle())

""" Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор. 
У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор. 
Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст
"""
# class Human:
    
#     def __init__(self, name: str, age: int, phone: int, mail: str) -> None:
#         self.name = name
#         self.__age = age
#         self.phone = phone
#         self.mail = mail
    
#     def birthday(self):
#         self.__age  += 1
    
#     def full_name(self):
#         return self.name
    
#     def info(self):
#         a = (f'Phone number is: {self.phone}, mail is: {self.mail}')
#         return a
    
#     def get_age(self):
#         return self.__age
# p1 = Human('Ivan', 25, 123456, 'ivan@mail.ru')
# print(p1.get_age(), p1.info() )
# p1.birthday()
# print(p1.get_age(), p1.info() )

""" Создайте класс Сотрудник. 
Воспользуйтесь классом человека из прошлого задания. 
У сотрудника должен быть:
шестизначный идентификационный номер
уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
"""
# class Colleague(Human):
#     def __init__(self, name: str, age: int, phone: int, mail: str, id : int) -> None:
#         super().__init__(name, age, phone, mail)
#         self.id = id
#         self.level = None
#     def acsess(self):
#         tmp = 0
#         for i in str(self.id):
#             tmp += int(i)
#         self.level = tmp % 7
# id_p = Colleague("Pol", 25, 321654, 'pol@mail.ru', 100258789)
# print(id_p.level, id_p.acsess(), id_p.level)

""" Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п. 
У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса. 
Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
"""

class Fauna:
    def __init__(self, name: str, blood_color: str):
        self.name = name
        self.blood_color = blood_color

    def eat(self):
        print(' Need food')


class Birds(Fauna):
    def __init__(self, name: str, blood_color: str, feathers: bool):
        super().__init__(name, blood_color)
        self.feathers = feathers

    def fly(self):
        print('I can fly!')


class Fishes(Fauna):
    def __init__(self, name: str, blood_color: str, gills: bool):
        super().__init__(name, blood_color)
        self.gills = gills


class Reptiles(Fauna):
    def __init__(self, name: str, blood_color: str, scales: bool):
        super().__init__(name, blood_color)
        self.scales = scales


bird = Birds('Кеша', 'красная', True)
bird.fly()
bird.eat()


"""Создайте класс Моя Строка, где:
📌 будут доступны все возможности str
📌 дополнительно хранятся имя автора строки и время создания (time.time)"""
import time

# class MyString(str):
#     """ MySrtring  осуществляет вывод строки, ее автора и время создания"""
#     def __init__(self, value: str, author: str):
#         self.value = value
#         self.author = author
        
#     def __new__(cls, value: str, author: str):
#         """ Создание нового экземпляра класса"""
#         instance = super().__new__(cls, value)
#         instance.author = author
#         instance.time = time.time()
#         return instance
    
#     def __str__(self) -> str:
#         """Вывод информации для пользователя"""
#         return f'My srtring is :{self.value}\n Time is: {time.time()} \n Author is: {self.author}'
   
#     def __repr__(self):
#         """Вывод близкого к созданию экземпляра класса представления"""
#         return f'MyString({self.value}, {time.time()},{self.author})'
 
# if __name__ == '__main__':
#     s = MyString("Весна пришла, весне дорогу!", "Тютчев")
#     print(s)
#     print(repr(s))
#     # print(s.time)
#     # print(s.author)

"""Создайте класс Архив, который хранит пару свойств. Например, число и строку. 
При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
list-архивы также являются свойствами экземпляра  """

# class Archive():
#     """ An Archive class with numbers and values. """
#     _one = None
#     def __init__(self, num: int, val: str) -> None:
#         """Added num and val parameters. """
#         self.num = num
#         self.val = val
    
#     def __new__(cls, *args, **kwargs):
#         """ Created mew lists for num and val, appended lists with numbers and values. """
#         if cls._one is None:
#             cls._one = super().__new__(cls)
#             cls._one.numbers = []
#             cls._one.values = []
#         else:
#             cls._one.numbers.append(cls._one.num)
#             cls._one.values.append(cls._one.val)
#         return cls._one
    
# s = Archive(123, '123355')
# print(s.numbers, s.values)

# s = Archive(5887, 'Hello')
# print(s.numbers, s.values)

# s = Archive(8952, 'Hi')
# print(s.numbers, s.values)

# #help(Archive)#вывод информации в терминал

"""Доработаем класс Архив из задачи 2.
📌 Добавьте методы представления экземпляра для программиста и для пользователя. """

# class Archive():
#     _one = None
#     def __init__(self, num: int, val: str) -> None:
#         self.num = num
#         self.val = val
    
#     def __new__(cls, *args, **kwargs):
        
#         if cls._one is None:
#             cls._one = super().__new__(cls)
#             cls._one.numbers = []
#             cls._one.values = []
#         else:
#             cls._one.numbers.append(cls._one.num)
#             cls._one.values.append(cls._one.val)
#         return cls._one
    
#     def __str__(self):
#         return f'Пары свойств из ранее созданных экземпляров "{self.num}", "{self.val}"'

#     def __repr__(self):
#          return f'Archive({self.num}, {self.val})'
    
# s = Archive(123, '123355')
# print(s.numbers, s.values)
# print(s)
# print(repr(s))

# s = Archive(5887, 'Hello')
# print(s.numbers, s.values)

# s = Archive(8952, 'Hi')
# print(s.numbers, s.values)

# print(s)#обязательно для вывода метода представления

"""Дорабатываем класс прямоугольник из прошлого семинара.Добавьте возможность сложения и вычитания. 
При этом должен создаваться новый экземпляр прямоугольника. Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений."""
class Rectangle:
    """ класс Rectangle принимает параметры длину и ширину прямоугольников, рассчитывает площадь, длину, 
    складывает и вычитает перимертры"""

    def __init__(self, side_a: float, side_b=None):
        """задает переменные класса"""
        self.side_a = side_a
        if side_b is None:
            self.side_b = side_a
        else:
            self.side_b = side_b

    def square_rectangle(self):
        """рассчитывает площадь прямоугольника"""
        return self.side_a * self.side_b

    def len_rectangle(self):
        """рассчитывает длину прямоугольника"""
        return (self.side_a + self.side_b) * 2
    
    def __add__(self, other):
        """складывает периметры прямоугольников"""
        a = self.side_a + other.side_a
        b = self.side_b + other.side_b
        return Rectangle(a, b)
    
    def __sub__(self, other):
        """вычитает периметры прямоугольников"""
        if self.len_rectangle() < other.len_rectangle():
            self, other = other, self
        a = self.side_a - other.side_a
        b = self.side_b - other.side_b
        return Rectangle(a, b)
    def __str__(self):
         return f'Первая строна "{self.side_a}", вторая строна "{self.side_b}"'

    def __repr__(self):
        return f'Rectangle({self.side_a}, {self.side_b})'


rect = Rectangle(5, 10)
#print(rect.len_rectangle(), rect.square_rectangle())
rec1 = Rectangle(4, 8)
rec2 = rect + rec1
print(rect.len_rectangle(),rec1.len_rectangle(),rec2.len_rectangle(),)
rec3 = rect - rec1
print(rect.len_rectangle(),rec1.len_rectangle(),rec3.len_rectangle())
print(f'Первая строна {rec2.side_a} вторая строна {rec2.side_b}')

print(rec1)
print(repr(rec1))

# print(f'{rec1 = }')

# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def __str__(self):
#         return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'
#     def __eq__(self, other):
#         first = sorted((self.a, self.b, self.c))
#         second = sorted((other.a, other.b, other.c))
#         return first == second
# one = Triangle(3, 4, 5)
# two = one
# three = Triangle(3, 4, 5)
# four = Triangle(4, 3, 5)
# print(f'{one == two = }')
# print(f'{one == three = }')
# print(f'{one == four = }')
# print(f'{one != one = }')




"""Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре."""
from string import ascii_letters

# def delfromtext(text: str):
    
#     a = ''
#     for char in text:
#         if char in ascii_letters or char == ' ':
#             a += char         
#     return a.lower()
# print(delfromtext('роме букв латинского. алфавита 123/ апраоп! hjjkg'))

import re
# def clean_text(text: str) -> str:
#     cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
#     return cleaned_text.lower()


# user_text = "Every утро i go на work! 12334_12"
# print(clean_text(user_text))

""" Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери
символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)"""

# def clean_text(text: str) -> str:
#     # 1 добавляем доктекст(в последнем надо добавить пробел после текста-см ф-цию)
#     """
#     >>> clean_text("hello world") 
#     'hello world'

#     >>> clean_text("HellO woRld")
#     'hello world'

#     >>> clean_text("hello, world...")
#     'hello world'

#     >>> clean_text("hello world ворлд") 
#     'hello world '

#     >>> clean_text("HellO !woRld, ворлд") 
#     'hello world '
#     """
#     cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
#     return cleaned_text.lower()

# # print(clean_text('hello world'))#  2 комментруем при прохождении теста
# # 1 закоментировать для получения текста в терминале, 2 раскоментировать для запуска
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)

""" Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)"""

import unittest

# def clean_text(text: str) -> str:
#         cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
#         return cleaned_text.lower()
# # print(clean_text('hello world'))

# class TestCaseName(unittest.TestCase):
    
#     def test_no_change(self):
#          self.assertEqual(clean_text("hello world"),'hello world')
    
#     def test_registr(self):
#          self.assertEqual(clean_text("HellO woRld"),'hello world') 

#     def test_no_punctuation(self):
#          self.assertEqual(clean_text("hello, world..."),'hello world')

#     def test_language(self):
#          self.assertEqual(clean_text("hello world ворлд"),'hello world ')
        
#     def test_all(self):
#          self.assertEqual(clean_text("HellO !woRld, ворлд"),'hello world ')    



# if __name__ == '__main__':
#     unittest.main(verbosity= 2)

""" Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)"""

#import pytest

# def clean_text(text: str) -> str:
#         cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
#         return cleaned_text.lower()

# def test_no_change():
#           assert clean_text("hello world") =='hello world', 'text 1'
    
# def test_registr():
#         assert clean_text("HellO woRld") =='hello world' , 'text 2'

# def test_no_punctuation():
#         assert clean_text("hello, world...") =='hello world', 'text 3'

# def test_language():
#         assert clean_text("hello world ворлд") =='hello world ', 'text 4'
    
# def test_all():
#         assert clean_text("HellO !woRld, ворлд") =='hello world ' , 'text 5' 


# if __name__ == '__main__':
#     pytest.main(['-vv'])

""" На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
📌 Напишите 3-7 тестов unittest для данного класса."""

class Rectangle:

    def __init__(self, side_a: float, side_b=None):
        self.side_a = side_a
        if side_b is None:
            self.side_b = side_a
        else:
            self.side_b = side_b

    def square_rectangle(self):
        return self.side_a * self.side_b

    def len_rectangle(self):
        return (self.side_a + self.side_b) * 2 #AssertionError: 18 != 36, если убрать 2

class TestCaseName(unittest.TestCase):
    def setUp(self) -> None:
        self.r1 = Rectangle(5, 15)
        self.r2 = Rectangle(4, 14)
            
    def test_square(self):
          self.assertEqual(self.r1.square_rectangle(), 75) 
    
    def test_len(self):
        self.assertEqual(self.r2.len_rectangle(), 36) 

if __name__ == '__main__':
    unittest.main(verbosity= 2)

# rect = Rectangle(5, 10)
# print(rect.len_rectangle(), rect.square_rectangle())
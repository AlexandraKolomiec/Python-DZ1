"""Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 📌 Напишите к ним тесты.
2-5 тестов на задачу в трёх вариантах:
○ doctest,
○ unittest,
○ pytest."""

""" Создайте класс окружность. 
Класс должен принимать радиус окружности при создании 
экземпляра. У класса должно быть два метода, возвращающие 
длину окружности и её площадь
"""
"""Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре."""

"""Doctest"""

from string import ascii_letters

# def delfromtext(text: str):
#     """ 
#     >>> delfromtext('кроме букв латинского. алфавита 123/ апраоп! hjjkg')
#     '      hjjkg'
   
#     >>> delfromtext('кромебуквлатинского.алфавита123/апраоп!hjjkg')
#     'hjjkg'

#     >>> delfromtext('kpome.букв латинского.алфавитa123/ апAаoп! hjjkg')
#     'kpome a ao hjjkg'
#      """
    
#     a = ''
#     for char in text:
#         if char in ascii_letters or char == ' ':
#             a += char         
#     return a.lower()
# print(delfromtext('kpome.букв латинского.алфавитa апAаoп! hjjkg'))

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)


"""Unittest"""

import unittest

def delfromtext(text: str):
    
    a = ''
    for char in text:
        if char in ascii_letters or char == ' ':
            a += char         
    return a.lower()
print(delfromtext('роме букв латинского. алфавита 123/ апраоп! hjjkg'))

class TestCaseName(unittest.TestCase):
    
    def test_no_change(self):
         self.assertEqual(delfromtext('кроме букв латинского. алфавита 123/ апраоп! hjjkg'),'      hjjkg')
    
    def test_no_spaces(self):
         self.assertEqual(delfromtext('кромебуквлатинского.алфавита123/апраоп!hjjkg'),'hjjkg') 

    def test_lathin_instead(self):
         self.assertEqual(delfromtext('kpome.букв латинского.алфавитa123/ апAаoп! hjjkg'),'kpome a ao hjjkg')


if __name__ == '__main__':
    unittest.main(verbosity= 2)
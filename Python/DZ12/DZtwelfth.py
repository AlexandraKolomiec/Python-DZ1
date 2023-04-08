"""Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам
 всех предметов вместе взятых."""

import csv

#Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв
class NameDescriptor:
        def __init__(self):
            self.value = ''

        def __get__(self, instance, owner):
            return self.value

        def __set__(self, instance, value):
            for name_word in value.split(' '):
                if not name_word.isalpha() or not name_word.istitle():
                    raise ValueError("Invalid full name: {}".format(value))
            self.value = value
#Создайте класс студента
class Student:
    full_name = NameDescriptor()

    def __init__(self, full_name, subjects_file):
        self.full_name = full_name
        self.subjects = self.load_subjects(subjects_file)
        self.grades = {subject: [] for subject in self.subjects}
        self.tests = {subject: [] for subject in self.subjects}
        self.test_score = {subject: [] for subject in self.subjects}
#Названия предметов должны загружаться из файла CSV при создании экземпляра.
    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', encoding='utf-8', newline='') as f:
            reader = csv.reader(f)
            subjects = next(reader)
            return subjects

# Другие предметы в экземпляре недопустимы.
    def add_grade(self, subject, grade):
            if subject not in self.subjects:
                raise ValueError(f"Subject '{subject}' not found.")
#Для каждого предмета можно хранить оценки (от 2 до 5)
            if not 2 <= grade <= 5:
                raise ValueError("Mark should be between 2 and 5.")
            self.grades[subject].append(grade)

#Для каждого предмета можно хранить результаты тестов (от 0 до 100)
    def add_test_score(self, subject, score):
            if subject not in self.subjects:
                raise ValueError(f"Subject '{subject}' not found.")
            if not 0 <= score <= 100:
                raise ValueError("Test result should be between  0 and 100.")
            self.test_score[subject].append(score)

#Также экземпляр должен сообщать средний балл по тестам для каждого предмета 
    def average_test_score(self, subject):
            """ Average test score for subject"""
            if subject not in self.subjects:
                raise ValueError(f"Subject '{subject}' not found.")
            if not self.test_score[subject]:
                raise ValueError("No result for this subject.")
            return f'Average test score for subject {subject}: {round(sum(self.test_score[subject])/len(self.test_score[subject]), 2)}'
#и по оценкам  всех предметов вместе взятых.
    def average_overall_grade(self):
        """ Average mark, all subjects """
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if not all_grades:
            raise ValueError("No marks to count.")
        return f'Average score for all subjects: {round(sum(all_grades) / len(all_grades), 2)}'

student = Student('Иванов Иван Иванович', 'students.csv')
# print(student)
student.add_grade("Math", 4)
student.add_grade("Math", 5)
student.add_test_score("Math", 88)
student.add_test_score("Math", 91)
student.add_grade("Art", 5)
student.add_grade("Art", 4)
student.add_grade("Art", 5)
student.add_grade("Physics", 4)
student.add_grade("Physics", 5)
student.add_grade("Physics", 4)
student.add_grade("Physics", 5)
student.add_test_score("Physics", 77)
student.add_test_score("Physics", 79)
student.add_test_score("Physics", 80)


# Получаем средний балл по тестам для предмета 
math_test_average = student.average_test_score("Physics")
print(math_test_average)

# Получаем средний балл по всем предметам
all_average = student.average_overall_grade()
print(all_average)
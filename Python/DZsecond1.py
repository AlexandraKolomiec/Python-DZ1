#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата

number: int = int(input("Enter number "))
number1: int = number
HEXADECIMAL = 16

print(hex(number))

number = number1
result: str = ""
while number > 0:
    double_num: int = number % HEXADECIMAL
    result = str(double_num) + result 
    number = number // HEXADECIMAL
print(result)
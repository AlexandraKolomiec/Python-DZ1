#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
#Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

import fractions

# f1 = fractions.Fraction(1, 3)
# print(f1)
# f2 = fractions.Fraction(3, 5)
# print(f2)
# print(f1 * f2)

firststring = input("Enter two number separated by /: ")
secondstring = input("Enter two number separated by /: ")

fr1 = fractions.Fraction(firststring)
print(fr1)
fr2 = fractions.Fraction(secondstring)
print(fr2)

print(fr1 + fr2)
print(fr1 * fr2)

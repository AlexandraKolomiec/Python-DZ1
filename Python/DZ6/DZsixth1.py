""" Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками. Функция в цикле вызывает
 загадывающую функцию, чтобы передать ей все свои загадки.
 """

from DZsixth1a import*
__all__ = ['mystery']

def mystery(chanse: int) -> str:
    USER = myst_list(int(input("Enter number from 0 to 2 ")))
    for i in range(chanse):
        
        print(USER[0]) 
        ans = input('Enter aswer:  ')
        if  ans == USER[1]:
            return 'You guess!!!'
        else:
            chanse + 1
            
    return 0
   

if __name__ == '__main__':
        
    print(mystery(2))



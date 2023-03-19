__all__ =['myst_list']

def myst_list(a:int):
    
    ml = {
        'На верхушке стебелька солнышко и облака' : 'ромашка',
        'Серые комочки на красненьком пруточке' : 'верба',
        'Зимой и летом одним цветом! ' : 'Елка',
    }
    m = (list(ml.items())[a])
    return m
        

if __name__ == '__main__':
    print(myst_list(int(input("Enter number from 0 to 2 "))))


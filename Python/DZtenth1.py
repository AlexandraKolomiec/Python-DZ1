""" Доработаем задачу 5. Создайте класс-фабрику. Класс принимает тип животного (название одного из созданных классов)
 и параметры для этого типа. Внутри класса создайте экземпляр на основе переданного типа и верните его из 
 класса-фабрики"""


class Birds:
    def __init__(self, name: str, has_blood: bool, feathers: bool):
        self.name = name
        self.has_blood = has_blood
        self.feathers = feathers or 'I live in the sky!'
        
    def fly(self):
        return 'I can fly !'


class Fish:
    def __init__(self, gills: bool):
        self.gills = gills or 'I live in the water!'
    def swim(self):
        return 'I can swim ~ ~'
        

class Reptiles:
    def __init__(self,  scales: bool):
        self.scales = scales or 'I live on earth!'
        

class Animals(Birds, Fish, Reptiles):
    def __init__(self, name = None, has_blood = None, feathers = None, gills = None, scales = None):
        Birds.__init__(self, name, has_blood, feathers)
        Fish.__init__(self, gills)
        Reptiles.__init__(self, scales)
        
    def has_tail(self):
        return 'I have tail!'
    
    def eat(self):
        return 'I eat food'

animal = Animals('Unicorn', False, False, True)
print(f'"My name is {animal.name}, {animal.feathers}, {animal.fly()}, {animal.has_tail()} ')

crocodile = Animals('Gena-crocodile', True, False, False, False)
print(f'"My name is {crocodile.name}, {crocodile.scales}, {crocodile.has_blood = },  {crocodile.has_tail()}, {crocodile.eat()} ')

fish = Animals('Booble', True, False, False, False)
print(f'"My name is {fish.name}, {fish.gills}, {fish.swim() } ')




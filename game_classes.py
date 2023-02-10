def decorator(func):
    def wrap(*args, **kwargs):
        print('------------------------------')
        func(*args, **kwargs)
        print('------------------------------')
    return wrap



class Warrior:
    def __init__(self, health=100, stamina=100):
        self.health = health
        self.stamina = stamina

    @decorator
    def introduces(self):
        print(f'Class: {self.__class__.__name__}\n'
              f'Health: {self.health}\n'
              f'Stamina: {self.stamina}')

    @decorator
    def heals(self, target):
        print(f'{self.__class__.__name__} применяет лечение травами'
              f' к {target.__class__.__name__}')
        target.health += 10
        self.stamina -= 20
        print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}\n'
              f'У {self.__class__.__name__} осталось {self.stamina} выносливости')

    @decorator
    def attacks(self, target):
        target.health -= 3
        print(f'{self.__class__.__name__} наносит урон мечом {target.__class__.__name__}')
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')



class Mage:

    @decorator
    def __init__(self, health=100, mana=60):
        self.health = health
        self.mana = mana

    @decorator
    def introduces(self):
        print(f'Class: {self.__class__.__name__}\n'
              f'Health: {self.health}\n'
              f'Mana: {self.mana}')

    @decorator
    def heals(self, target):
        print(f'{self.__class__.__name__} применяет заклинание лечения'
              f' к {target.__class__.__name__}')
        target.health += 10
        self.mana -= 20
        print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}\n'
              f'У {self.__class__.__name__} осталось {self.mana} мана')


    @decorator
    def attacks(self, target):
        target.health -= 3
        print(f'{self.__class__.__name__} наносит урон магией {target.__class__.__name__}')
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')



class Archer:
    def __init__(self):
        self.health = 50
        self.arrows_count = 20


unit1 = Warrior(100, 50)
unit2 = Warrior(70, 120)
unit3 = Mage(60, 100)
unit4 = Mage(health=50, mana=110)

unit1.introduces()
unit4.introduces()

unit4.attacks(unit1)

unit1.introduces()
unit4.introduces()

print(unit1.__dict__)
print(unit2.__dict__)
print(unit3.__dict__)
print(unit4.__dict__)

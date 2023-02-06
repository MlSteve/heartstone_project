class Warrior:
    def __init__(self):
        self.health = 100
        self.stamina = 100

class Mage:
    def __init__(self):
        self.health = 100
        self.mana = 60

class Archer:
    def __init__(self):
        self.health = 50
        self.arrows_count = 20

unit1 = Warrior()
unit2 = Warrior()
unit3 = Mage()
unit4 = Archer()


print(unit1.__dict__)
print(unit2.__dict__)
print(unit3.__dict__)
print(unit4.__dict__)
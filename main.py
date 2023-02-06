class Warrior:
    def __init__(self):
        self.health = 100
        self.stamina = 100

class Mage:
    def __init__(self):
        self.health = 100
        self.mana = 60

unit1 = Warrior()
unit2 = Warrior()
unit3 = Mage()


print(unit1.__dict__)
print(unit2.__dict__)
print(unit3.__dict__)
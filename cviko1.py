class Warrior:

    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
    
    def zautoc(self):
        print (f"{self.name} zautocil za {self.dmg} dmg")

oWarrior = Warrior("Thelegend", 20, 15)

print(oWarrior.name)
oWarrior.zautoc()
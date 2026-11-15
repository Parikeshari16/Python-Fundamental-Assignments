class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def display(self):
        print("Name:", self.name)
        print("Health:", self.health)

class Warrior(Character):
    def attack(self):
        print(self.name, "attacks with a sword")

class Mage(Character):
    def attack(self):
        print(self.name, "attacks with magic")

w = Warrior("Thor", 100)
m = Mage("Merlin", 80)

w.display()
w.attack()

m.display()
m.attack()
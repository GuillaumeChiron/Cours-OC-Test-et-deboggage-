from type_class import Mage

class Player:
    def __init__(self, name, type_class):
        self.name = name
        self.type_class = type_class
        self.health_point = 100
        self.mana_point = 10

    def drink_potion(self):
        self.mana_point += self.type_class.add_mana()

    def use_spell(self):
        self.mana_point += self.type_class.delete_mana()

    def get_infos(self):
        return {
            "Name": self.name,
            "Type_class": self.type_class.name,
            "Health_point": self.health_point,
            "Mana": self.mana_point
        }

class1 = Mage()
player1 = Player("guitou", class1)

print(player1.get_infos())

player1.use_spell()

print(player1.get_infos())
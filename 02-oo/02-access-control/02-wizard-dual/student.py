class Wizard:
    def __init__(self, name):
        self.__mana = 45
        self.__health = 65
        self.name = name

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health

    def get_fireballed(self):
        self.__mana -= 30

    def drink_mana_potion(self):
        self.__nana += 40

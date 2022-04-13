from pokemon import Pokemon


class Player():
    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.inventory = [{
            "pokeballs": 1,
            "potions": 1
        }]

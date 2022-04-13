import requests


class Pokemon():

    def __init__(self, name, hp, maxHP, moves, element):
        self.name = name
        self.hp = hp
        self.maxHP = hp
        self.moves = [moves]
        self.element = element

import imp
import requests

from pokemon import*
from moves import *

pokeURL = "https://pokeapi.co/api/v2/pokemon/"
# getPoke = ["rattata","pidgey"]
poke1 = requests.get(f"{pokeURL}rattata").json()
poke2 = requests.get(f"{pokeURL}pidgey").json()

monstDict = {}
pokeList = []

pokeList.append(poke1)
pokeList.append(poke2)


def createPokemon(pokeList):

    i = 0
    for poke in pokeList:

        name = poke['forms'][0]['name']
        hp = poke['stats'][0]['base_stat']
        maxHP = hp
        element = poke['types'][0]['type']['name']
        moves = enemyMoves[0]

        monstDict['poke_'+str(i)] = (Pokemon(name, hp, maxHP, moves, element))
        i += 1


createPokemon(pokeList)

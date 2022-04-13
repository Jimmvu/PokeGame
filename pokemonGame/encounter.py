
import random
from monsters import *
from player import *
from moves import *

# Pulls from the pokeList and selects one at random to battle


def randomEncounter(newPlayer):
    randomNum = random.randint(0, len(pokeList)-1)
    strKey = f"poke_{randomNum}"
    randPoke = monstDict[strKey]

    print(
        f"You ran into a {randPoke.name} and have no choice but to fight")
    battle(randPoke, newPlayer)

# Enter Battle


def battle(randPoke, newPlayer):
    battleState = True
    userInput = ""
    currentPokemon = newPlayer.pokemon[0]
    while(battleState == True):
        while(userInput not in ["attack", "pokemon", "items", "run"]):
            print(f"Enemy {randPoke.name}: {randPoke.hp} / {randPoke.maxHP}")
            print("What will you do?")
            print(
                f"{currentPokemon.name}: hp {currentPokemon.hp} / {currentPokemon.maxHP}")
            print("=====================")
            print("| Attack    Pokemon |")
            print("| Items       Run   |")
            print("=====================")

            userInput = input("\n>").lower()
            if userInput == "run":
                battleState = run(currentPokemon, randPoke)
                print(f"battleState: {battleState}")
                if(battleState == True):
                    userInput = ""
            elif userInput == "attack":
                Attack(currentPokemon, randPoke)
                if(randPoke.hp <= 0):
                    print(f"Enemy {randPoke.name} fainted")
                    battleState = False
                    randPoke.hp = randPoke.maxHP
                else:
                    userInput = ""
            elif userInput == "items":
                showItems(newPlayer, currentPokemon)
                userInput = ""
            elif userInput == "pokemon":
                selectPokemon(currentPokemon, newPlayer)
                userInput = ""


def selectPokemon(currentPokemon, newPlayer):
    userInput = ""
    listPokemon = []
    for pokemon in newPlayer.pokemon:
        listPokemon.append(f"{pokemon.name} hp: {pokemon.hp}")
    while userInput not in listPokemon:
        print("Choose a pokemon to switch out to")
        print(listPokemon)
        userInput = input("> ")

# Attack Method


def Attack(currentPokemon, randPoke):
    userInput = ""
    # Grabs the moves list of move dictionaries and parses the keys as a list
    listAbilities = currentPokemon.moves[0].keys()

    while(userInput not in listAbilities):
        # Print out usable moves and their relative pp:
        for atk in currentPokemon.moves:
            for name in atk:
                print(
                    f"{atk[name]['name']} pp: {atk[name]['pp']} / {atk[name]['maxPP']}")

        print("---------------------------\nChoose a Move\n---------------------------")

        userInput = input("\n>").lower()

    damage = pokeMoves[0][userInput]["dmg"]
    print(damage)
    print(
        f"{currentPokemon.name} used {userInput} and dealt {damage} damage")
    randPoke.hp -= damage
    currentPokemon.moves[0][userInput]['pp'] -= 1
    enemyAttacks(currentPokemon, randPoke)

# Run Method


def run(currentPokemon, randPoke):
    runChance = random.choice([True, False])
    print(f"runChance: {runChance}")
    if runChance == True:
        print("You escaped")
        return False
    else:
        print("You failed to escape!")
        enemyAttacks(currentPokemon, randPoke)
        return True

# Check Items


def showItems(newPlayer, currentPokemon):
    print(newPlayer.inventory)
    print("What do you want to use")
    userInput = input("> ").lower()
    print(str(newPlayer.inventory[0]["potions"]), "Huh")
    try:
        # Using a potion
        if userInput == "potions" and newPlayer.inventory[0][userInput] > 0:
            print(f"You used a potion to heal {currentPokemon.name}")
            newPlayer.inventory[0][userInput] -= 1
            currentPokemon.hp = currentPokemon.maxHP
        # Using a Pokeball
        elif userInput == "pokeballs" and newPlayer.inventory[0][userInput] > 0:
            print(f"You used a pokeball")
            newPlayer.inventory[0][userInput] -= 1
            # catchPokemon(newPlayer,currenPokemon,randPoke)
    except:
        print("You cant do that")
        return

# Catching the Pokemon


def catchPokemon(newPlayer, currentPokemon, randPoke):
    tier1 = [1, 2, 3, 4, 5]

# Enemy Attacks


def enemyAttacks(currentPokemon, randPoke):
    if randPoke.hp > 0:
        print(f"{randPoke.name} does 5 damage to {currentPokemon.name}")
        currentPokemon.hp -= 5

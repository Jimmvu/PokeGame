from copy import copy
import random
import sys

from monsters import *
from player import *
from moves import *
from userutils import *

# Pulls from the pokeList and selects one at random to battle


def randomEncounter(newPlayer):

    randomNum = random.randint(0, len(pokeList)-1)
    strKey = f"poke_{randomNum}"
    randPoke = monstDict[strKey]

    print(
        f"You ran into a {randPoke.name} and have no choice but to fight")
    enterClear()
    battle(randPoke, newPlayer)

# Enter Battle


def battle(randPoke, newPlayer):
    battleState = True
    userInput = ""
    while(battleState == True):
        while(userInput not in ["attack", "pokemon", "items", "run"]):
            clear()
            currentPokemon = newPlayer.pokemon[0]
            print(f"Enemy {randPoke.name}: {randPoke.hp} / {randPoke.maxHP}")
            print("What will you do?")
            print(
                f"{currentPokemon.name}: hp {currentPokemon.hp} / {currentPokemon.maxHP}")
            print("=====================")
            print("| Attack    Pokemon |")
            print("| Items       Run   |")
            print("=====================")

            userInput = input("\n>").lower()
            # Player runs
            if userInput == "run":
                battleState = run(currentPokemon, randPoke)
                print(f"battleState: {battleState}")
                if(battleState == True):
                    userInput = ""

            # Player attacks
            elif userInput == "attack":
                Attack(currentPokemon, randPoke)
                # TODO
                # Need to seperate the check method to work with when enemy attacks when you run or use item / bug

                # Enemy pokemon faints
                if(randPoke.hp <= 0):
                    print(f"Enemy {randPoke.name} fainted")
                    battleState = False
                    randPoke.hp = randPoke.maxHP
                # Current Pokemon faints
                elif currentPokemon.hp < 0:
                    print(f"{currentPokemon.name} has fainted")
                    anyLeft = []
                    # Check if there are any pokemon left to play
                    for poke in newPlayer.pokemon:
                        if poke.hp > 0:
                            anyLeft.append(True)
                        else:
                            anyLeft.append(False)
                    if True in anyLeft:
                        selectPokemon(currentPokemon, newPlayer)
                    # If not, end game
                    else:
                        gameEnd()
                else:
                    userInput = ""

            # Player uses items
            elif userInput == "items":
                battleState = showItems(
                    newPlayer, currentPokemon, randPoke)
                enterClear()
                if battleState == True:
                    userInput = ""

            # Player switches pokemon
            elif userInput == "pokemon":
                selectPokemon(currentPokemon, newPlayer)
                userInput = ""


def selectPokemon(currentPokemon, newPlayer):
    userInput = ""
    listPokemon = []
    # List current pokemon
    for pokemon in newPlayer.pokemon:
        listPokemon.append(f"{pokemon.name} {pokemon.hp} / {pokemon.maxHP}")
    # Player chooses index of pokemon to be swapped
    while userInput not in range(0, len(listPokemon)):
        index = 0
        print(f"Choose a pokemon to switch out to: 0 - {len(listPokemon)}")
        for element in listPokemon:
            print(f"{index} : {element}")
            index += 1
        # Try if user enters a string
        try:
            userInput = int(input("> "))
        except:
            print("Invalid Input")
    # If that pokemon's health is greater than 0 switch
    if(newPlayer.pokemon[userInput].hp > 0):
        print(
            f"You switched out {currentPokemon.name} for {newPlayer.pokemon[userInput].name}")
        newPlayer.pokemon[0], newPlayer.pokemon[userInput] = newPlayer.pokemon[userInput], newPlayer.pokemon[0]
        enterClear()
    # Else recall the function
    else:
        print("You can't do that")
        enterClear()
        selectPokemon(currentPokemon, newPlayer)


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
    print(
        f"{currentPokemon.name} used {userInput} and dealt {damage} damage")
    randPoke.hp -= damage
    currentPokemon.moves[0][userInput]['pp'] -= 1
    enterClear()
    enemyAttacks(currentPokemon, randPoke)
    enterClear()

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


def showItems(newPlayer, currentPokemon, randPoke):
    battleState = True
    print(newPlayer.inventory)
    print("What do you want to use")
    userInput = input("> ").lower()
    print(str(newPlayer.inventory[0]["potions"]))
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
            battleState = catchPokemon(newPlayer, currentPokemon, randPoke)
    except Exception as e:
        print("You can't do that")
        return True
    else:
        if battleState:
            return True
        else:
            randPoke.hp = randPoke.maxHP
            return False

# Catching the Pokemon


def catchPokemon(newPlayer, currentPokemon, randPoke):
    tier = []
    newPoke = copy(randPoke)
    # Check randPoke health
    if randPoke.hp > randPoke.maxHP/2:
        tier = [1, 2, 3, 4, 5]
    else:
        tier = [3, 4, 5]

    # Check the user pokemon if full
    if random.choice(tier) >= 4:
        if len(newPlayer.pokemon) == 5:
            print(f"{randPoke.name} has been caught and added to your PC")
            enterClear()
            return False
        else:
            print(f"{randPoke.name} has been caught")
            newPlayer.pokemon.append(newPoke)
            enterClear()
            return False

    # Fail the roll
    else:
        print(f"You failed to catch {randPoke.name}")
        enterClear()
        enemyAttacks(currentPokemon, randPoke)
        return True


# Enemy Attacks


def enemyAttacks(currentPokemon, randPoke):
    # TODO
    # Make it not hardcoded
    if randPoke.hp > 0:
        print(f"{randPoke.name} does 5 damage to {currentPokemon.name}")
        currentPokemon.hp -= 5


# Game End
def gameEnd():
    print("You have no more pokemon left to play, you fainted")
    enterClear()
    sys.exit()

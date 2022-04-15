import random

from pokemon import *
from player import *
from routes import *
from monsters import *
from encounter import *
from playsound import *


newPlayer = Player("Player")
pikachu = Pokemon("Pikachu", 30, 30, pokeMoves[0], "Electric")
newPlayer.pokemon.append(pikachu)


def showInstructions():
    # print a main menu and the commands
    print('''
    Pokemon Game
    Objective: Get to Lavender town with 3 or more pokemon
    ========
    Commands:
    go [direction]
    get [item]
    pokemon
    items
    ''')
    enterClear()


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(newPlayer.inventory))
    # print an item if there is one
    if "item" in route31[currentRoom]:
        print('You see a ' + route31[currentRoom]['item'])
    print("---------------------------")


def showPokemon():
    clear()
    for poke in newPlayer.pokemon:
        print(f"{poke.name} HP: {poke.hp} / {poke.maxHP}")
    enterClear()


# A dictionary linking a room to other rooms
# start the player in the Hall
currentRoom = 'S Forest'

showInstructions()

# loop forever
while True:
    clear()
    if len(newPlayer.pokemon) >= 3 and currentRoom == 'Forest End':
        print("You caught enough pokemon and are ready for your next Adventure")
        print("YOU WIN")
        enterClear()
        sys.exit()
    showStatus()
    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in route31[currentRoom]:
            # set the current room to the new room
            currentRoom = route31[currentRoom][move[1]]
            if random.choice([True, False]) == True:
                randomEncounter(newPlayer)
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')
            enterClear()

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in route31[currentRoom] and move[1] in route31[currentRoom]['item']:
            # add the item to their inventory
            item = route31[currentRoom]['item']
            print(move[1] + ' got!')
            newPlayer.inventory[0][item + 's'] += 1
            # delete the item from the room
            del route31[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    if move[0] == 'pokemon':
        showPokemon()

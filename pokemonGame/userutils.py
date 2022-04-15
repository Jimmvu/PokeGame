import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def enterClear():
    input("Press any key to continue")
    os.system('cls' if os.name == 'nt' else 'clear')
